"""Response agent: generate customer-facing answer from context."""

from langchain_core.messages import HumanMessage, SystemMessage

from contracts import SupportContext
from data import format_order_details
from llm_client import create_llm


INTENT_HANDLERS = {
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
Provide helpful, accurate information and guide the customer to the right resources.""",
}


def run_response_agent(context: SupportContext) -> SupportContext:
    llm = create_llm()

    system_prompt = INTENT_HANDLERS.get(context.intent, INTENT_HANDLERS["general_inquiry"])
    order_id = context.order_id or "not provided"

    prompt = f"""Customer message: "{context.message}"
Order ID: {order_id}
"""

    if context.order_data:
        prompt += f"""

REAL ORDER DATA FROM DATABASE:
{format_order_details(context.order_data)}

Use this actual order information in your response. Be specific about status, tracking, delivery dates, and items.
"""
    else:
        prompt += "\nNote: No order found in database. Provide general guidance and ask for order confirmation."

    prompt += (
        "\n\nGenerate a helpful, empathetic, and professional response. "
        "Keep it clear and concise (3-5 sentences). "
        "Include specific action items or next steps when relevant."
    )

    context.response = llm.invoke(
        [SystemMessage(content=system_prompt), HumanMessage(content=prompt)]
    ).content.strip()

    return context
