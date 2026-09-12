"""Tests for the normalize_whitespace string helper."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from text_utils import normalize_whitespace


def test_normalize_whitespace_collapses_inner_and_trims() -> None:
    assert normalize_whitespace("  a   b  ") == "a b"


def test_normalize_whitespace_empty_string() -> None:
    assert normalize_whitespace("") == ""


def test_normalize_whitespace_single_word() -> None:
    assert normalize_whitespace("  hello  ") == "hello"


def test_normalize_whitespace_tabs_and_newlines() -> None:
    assert normalize_whitespace("\t  a\n  b \t") == "a b"
