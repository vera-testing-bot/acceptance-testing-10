"""Trivial module so an acceptance shard repo has code to change."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def cancel_status(state: str) -> str:
    """Map an issue state to its Vera lifecycle status.

    A closed issue corresponds to a canceled run.
    """
    if state == "closed":
        return "canceled"
    return "active"
