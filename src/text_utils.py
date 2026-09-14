"""String helpers for normalizing whitespace."""


def normalize_whitespace(text: str) -> str:
    """Collapse runs of whitespace into single spaces and strip the ends."""
    return " ".join(text.split())
