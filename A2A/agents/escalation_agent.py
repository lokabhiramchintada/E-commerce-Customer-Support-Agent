"""Escalation agent: determine if a human handoff is required."""

from contracts import ISSUE_TYPES, SupportContext


def run_escalation_agent(context: SupportContext) -> SupportContext:
    needs_escalation = False

    if context.confidence < 0.6:
        needs_escalation = True

    if context.sentiment == "negative" and context.intent in ["damaged_item", "refund_request"]:
        urgent_keywords = [
            "urgent",
            "immediately",
            "asap",
            "terrible",
            "worst",
            "lawsuit",
            "legal",
            "angry",
            "furious",
            "unacceptable",
        ]
        if any(keyword in context.message.lower() for keyword in urgent_keywords):
            needs_escalation = True

    issue_count = sum(
        1
        for issue_type in ISSUE_TYPES
        if any(word in context.message.lower() for word in issue_type.split("_"))
    )
    if issue_count >= 3:
        needs_escalation = True

    context.needs_escalation = needs_escalation
    return context
