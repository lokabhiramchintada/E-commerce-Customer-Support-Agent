"""Intent agent: classify message intent and extract metadata."""

from langchain_core.messages import HumanMessage

from contracts import ISSUE_TYPES, SupportContext
from llm_client import create_llm


def run_intent_agent(context: SupportContext) -> SupportContext:
    llm = create_llm()
    message = context.message

    prompt = f"""You are a customer support intent classifier for an e-commerce platform.

Analyze this customer message and classify it into ONE of these categories:
- delivery_inquiry: Questions about shipping, tracking, delivery time
- refund_request: Requests for money back, return requests
- damaged_item: Reports of broken, defective, or damaged products
- order_cancellation: Requests to cancel an order
- payment_issue: Problems with payment, billing, charges
- general_inquiry: General questions, account issues, other

Only use one of these exact intents: {", ".join(ISSUE_TYPES)}

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

    result = llm.invoke([HumanMessage(content=prompt)]).content

    for line in result.strip().split("\n"):
        if line.startswith("INTENT:"):
            context.intent = line.split(":", 1)[1].strip().lower()
        elif line.startswith("SENTIMENT:"):
            context.sentiment = line.split(":", 1)[1].strip().lower()
        elif line.startswith("CONFIDENCE:"):
            try:
                context.confidence = float(line.split(":", 1)[1].strip())
            except ValueError:
                context.confidence = 0.8
        elif line.startswith("ORDER_ID:"):
            order_str = line.split(":", 1)[1].strip().lower()
            if order_str and order_str != "none":
                context.order_id = order_str

    if context.intent not in ISSUE_TYPES:
        context.intent = "general_inquiry"

    return context
