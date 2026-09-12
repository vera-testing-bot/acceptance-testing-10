"""String helpers for normalizing whitespace."""


def normalize_whitespace(text: str) -> str:
    """Collapse runs of whitespace into single spaces and trim the ends."""
    return " ".join(text.split())
