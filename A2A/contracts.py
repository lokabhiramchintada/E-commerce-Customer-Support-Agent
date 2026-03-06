"""Shared contracts for A2A agent handoffs."""

from dataclasses import dataclass
from typing import Any


ISSUE_TYPES = [
    "delivery_inquiry",
    "refund_request",
    "damaged_item",
    "order_cancellation",
    "payment_issue",
    "general_inquiry",
]


@dataclass
class SupportContext:
    message: str
    intent: str = "general_inquiry"
    sentiment: str = "neutral"
    confidence: float = 0.8
    order_id: str | None = None
    order_data: dict[str, Any] | None = None
    response: str = ""
    needs_escalation: bool = False

    def to_public_response(self) -> dict[str, Any]:
        return {
            "response": self.response,
            "intent": self.intent,
            "sentiment": self.sentiment,
            "needs_escalation": self.needs_escalation,
            "confidence": self.confidence,
            "order_id": self.order_id,
        }
