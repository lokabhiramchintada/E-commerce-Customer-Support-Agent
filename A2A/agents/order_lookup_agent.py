"""Order lookup agent: fetch order details using extracted order ID."""

from contracts import SupportContext
from data import get_order


def run_order_lookup_agent(context: SupportContext) -> SupportContext:
    if context.order_id:
        context.order_data = get_order(context.order_id)
    return context
