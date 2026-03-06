"""True A2A orchestrator (no LangGraph) using explicit agent handoffs."""

from agents.escalation_agent import run_escalation_agent
from agents.intent_agent import run_intent_agent
from agents.order_lookup_agent import run_order_lookup_agent
from agents.response_agent import run_response_agent
from contracts import SupportContext


def process_customer_message(message: str) -> dict:
    context = SupportContext(message=message)

    context = run_intent_agent(context)
    context = run_order_lookup_agent(context)
    context = run_response_agent(context)
    context = run_escalation_agent(context)

    return context.to_public_response()
