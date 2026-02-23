"""
E-commerce Customer Support Agent using LangGraph
Workflow: Message → Intent Classification → Routing → Response → Escalation Check
"""

from typing import TypedDict, Literal, Annotated
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
from data import get_order, format_order_details, ORDERS, PRODUCTS, CUSTOMERS

# Load environment variables
load_dotenv()

# Initialize Gemini 2.5 Flash Lite
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)


class SupportState(TypedDict):
    """State of the customer support workflow"""
    message: str
    intent: str
    sentiment: str
    needs_escalation: bool
    response: str
    confidence: float
    order_id: str | None
    order_data: dict | None


# Issue types we support
ISSUE_TYPES = [
    "delivery_inquiry",
    "refund_request",
    "damaged_item",
    "order_cancellation",
    "payment_issue",
    "general_inquiry"
]


def classify_intent(state: SupportState) -> SupportState:
    """
    Classify the customer's intent from their message
    """
    message = state["message"]
    
    prompt = f"""You are a customer support intent classifier for an e-commerce platform.

Analyze this customer message and classify it into ONE of these categories:
- delivery_inquiry: Questions about shipping, tracking, delivery time
- refund_request: Requests for money back, return requests
- damaged_item: Reports of broken, defective, or damaged products
- order_cancellation: Requests to cancel an order
- payment_issue: Problems with payment, billing, charges
- general_inquiry: General questions, account issues, other

Also determine:
1. Sentiment (positive/neutral/negative)
2. Confidence level (0.0 to 1.0)
3. Order ID if mentioned (format: #12345 or ORD-12345 or just numbers)

Customer message: "{message}"

Respond in this exact format:
INTENT: [category]
SENTIMENT: [sentiment]
CONFIDENCE: [number]
ORDER_ID: [id or none]"""

    response = llm.invoke([HumanMessage(content=prompt)])
    result = response.content
    
    # Parse the response
    lines = result.strip().split('\n')
    intent = "general_inquiry"
    sentiment = "neutral"
    confidence = 0.8
    order_id = None
    
    for line in lines:
        if line.startswith("INTENT:"):
            intent = line.split(":", 1)[1].strip().lower()
        elif line.startswith("SENTIMENT:"):
            sentiment = line.split(":", 1)[1].strip().lower()
        elif line.startswith("CONFIDENCE:"):
            try:
                confidence = float(line.split(":", 1)[1].strip())
            except:
                confidence = 0.8
        elif line.startswith("ORDER_ID:"):
            order_str = line.split(":", 1)[1].strip().lower()
            if order_str != "none" and order_str:
                order_id = order_str
    
    state["intent"] = intent
    state["sentiment"] = sentiment
    state["confidence"] = confidence
    state["order_id"] = order_id
    
    return state


def route_to_handler(state: SupportState) -> SupportState:
    """
    Route the message to the appropriate handler based on intent
    Look up order data if order ID was detected
    """
    order_id = state.get("order_id")
    order_data = None
    
    if order_id:
        # Try to find order in database
        order_data = get_order(order_id)
        if order_data:
            state["order_data"] = order_data
    
    return state


def generate_response(state: SupportState) -> SupportState:
    """
    Generate a context-aware response based on the classified intent
    """
    intent = state["intent"]
    message = state["message"]
    order_id = state.get("order_id", "not provided")
    order_data = state.get("order_data")
    
    # Create intent-specific system prompts
    handlers = {
        "delivery_inquiry": """You are a helpful delivery support specialist. 
Provide tracking information guidance, typical delivery times, and reassurance.
Be specific about next steps the customer should take.""",
        
        "refund_request": """You are a refunds specialist for an e-commerce platform.
Explain the refund process clearly, mention typical processing times (5-7 business days),
and provide information about how to initiate a return if needed.""",
        
        "damaged_item": """You are a quality assurance specialist.
Apologize sincerely for the damaged item, explain the replacement/refund process,
and ask for photos of the damage if not already provided. Prioritize customer satisfaction.""",
        
        "order_cancellation": """You are an order management specialist.
Explain how to cancel an order, mention any time constraints (e.g., before shipping),
and describe the refund timeline if applicable.""",
        
        "payment_issue": """You are a billing support specialist.
Address payment concerns carefully, verify charge details, explain common payment issues,
and provide clear steps to resolve the problem.""",
        
        "general_inquiry": """You are a friendly customer support representative.
Provide helpful, accurate information and guide the customer to the right resources."""
    }
    
    system_prompt = handlers.get(intent, handlers["general_inquiry"])
    
    # Build context with order data if available
    context = f"""Customer message: "{message}"
Order ID: {order_id}
"""
    
    if order_data:
        context += f"""

REAL ORDER DATA FROM DATABASE:
{format_order_details(order_data)}

Use this actual order information in your response. Be specific about status, tracking, delivery dates, and items.
"""
    else:
        context += "\nNote: No order found in database. Provide general guidance and ask for order confirmation."
    
    context += "\n\nGenerate a helpful, empathetic, and professional response. Keep it clear and concise (3-5 sentences).\nInclude specific action items or next steps when relevant."
    
    user_prompt = context

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])
    
    state["response"] = response.content.strip()
    
    return state


def check_escalation(state: SupportState) -> SupportState:
    """
    Determine if the case needs human escalation
    """
    message = state["message"]
    intent = state["intent"]
    confidence = state["confidence"]
    sentiment = state["sentiment"]
    
    # Escalation criteria
    needs_escalation = False
    
    # Low confidence in classification
    if confidence < 0.6:
        needs_escalation = True
    
    # Very negative sentiment with certain intents
    if sentiment == "negative" and intent in ["damaged_item", "refund_request"]:
        # Check for urgency keywords
        urgent_keywords = ["urgent", "immediately", "asap", "terrible", "worst", 
                          "lawsuit", "legal", "angry", "furious", "unacceptable"]
        if any(keyword in message.lower() for keyword in urgent_keywords):
            needs_escalation = True
    
    # Complex multi-issue messages
    issue_count = sum(1 for issue_type in ISSUE_TYPES 
                     if any(word in message.lower() 
                           for word in issue_type.split('_')))
    if issue_count >= 3:
        needs_escalation = True
    
    state["needs_escalation"] = needs_escalation
    
    return state


def create_support_agent():
    """
    Create the LangGraph workflow for customer support
    """
    # Create the state graph
    workflow = StateGraph(SupportState)
    
    # Add nodes for each step
    workflow.add_node("classify_intent", classify_intent)
    workflow.add_node("route_to_handler", route_to_handler)
    workflow.add_node("generate_response", generate_response)
    workflow.add_node("check_escalation", check_escalation)
    
    # Define the flow
    workflow.set_entry_point("classify_intent")
    workflow.add_edge("classify_intent", "route_to_handler")
    workflow.add_edge("route_to_handler", "generate_response")
    workflow.add_edge("generate_response", "check_escalation")
    workflow.add_edge("check_escalation", END)
    
    # Compile the graph
    agent = workflow.compile()
    
    return agent


def process_customer_message(message: str) -> dict:
    """
    Process a customer message through the support agent
    
    Args:
        message: Customer's message text
        
    Returns:
        dict with response, intent, needs_escalation, and other metadata
    """
    agent = create_support_agent()
    
    # Initial state
    initial_state = {
        "message": message,
        "intent": "",
        "sentiment": "",
        "needs_escalation": False,
        "response": "",
        "confidence": 0.0,
        "order_id": None,
        "order_data": None
    }
    
    # Run the workflow
    result = agent.invoke(initial_state)
    
    return {
        "response": result["response"],
        "intent": result["intent"],
        "sentiment": result["sentiment"],
        "needs_escalation": result["needs_escalation"],
        "confidence": result["confidence"],
        "order_id": result["order_id"]
    }


if __name__ == "__main__":
    # Test the agent
    test_messages = [
        "Where is my order #12345? It's been 2 weeks!",
        "I received a broken phone. This is unacceptable!",
        "Can I get a refund for order ORD-98765?",
        "How do I cancel my order?",
    ]
    
    for msg in test_messages:
        print(f"\n{'='*60}")
        print(f"Customer: {msg}")
        print(f"{'='*60}")
        result = process_customer_message(msg)
        print(f"Intent: {result['intent']}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Escalation needed: {result['needs_escalation']}")
        print(f"\nAgent Response:\n{result['response']}")
