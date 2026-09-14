"""Tests for the normalize_whitespace string helper."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from text_utils import normalize_whitespace


def test_normalize_collapses_inner_whitespace() -> None:
    assert normalize_whitespace("  a   b  ") == "a b"


def test_normalize_empty_string() -> None:
    assert normalize_whitespace("") == ""
