import pytest
from src.core import estimate_tokens, split_context, CHARS_PER_TOKEN

class TestTokenEstimation:
    @pytest.mark.parametrize("text, expected",[
        ("A" * (CHARS_PER_TOKEN * 10), 10),                 # Scalable check
        ("A" * 7, 1),                                       # Floor division check
        ("A", 0),                                           # Small string check
        (" " * (CHARS_PER_TOKEN * 5), 5),                   # Whitespace check
        ("", 0),                                            # Empty string
        (None, 0),                                          # Null safety
    ])
    def test_estimate_tokens(self, text, expected):
        """
        Ensure token estimation follows floor division based on CHARS_PER_TOKEN.
        """
        assert estimate_tokens(text) == expected

class TestContextSplitting:
    @pytest.mark.parametrize("context, limit, expected", [
        ("ABCDEFGHIJKL", 1, ["ABCD", "EFGH", "IJKL"]),      # The happy path
        ("AAAAB", 1, ["AAAA", "B"]),                        # Right above the limit
        ("", 1, []),                                        # Empty string
    ])
    def test_split_context(self, context, limit, expected):
        """
        Ensure text is divided into chunks as expected based on the number of
        tokens per chunk limit.
        """
        assert split_context(context, limit) == expected

    def test_split_zero_limit_fails(self):
        # This documents that the function currently crashes on limit=0
        with pytest.raises(ValueError):
            split_context("some text", 0)

    def test_split_null_fail(self):
        # This documents that the function currently crashes on context=None
        with pytest.raises(TypeError):
            split_context(None, 1)