import pytest

from segment_display import parse_input_line


parse_signal_pattern_test_data = [
    ("abc def gab cde fgabc defg abcde fga bcdef gabcd | edcba gfe dcba gfedc",
     ["abc", "def", "gab", "cde", "fgabc", "defg", "abcde", "fga", "bcdef", "gabcd"],
     ["edcba", "gfe", "dcba", "gfedc"])
]


@pytest.mark.parametrize("input_data, expected_signal_pattern, expected_display_values", parse_signal_pattern_test_data)
def test_input_parser(input_data, expected_signal_pattern, expected_display_values):
    signal_pattern, display_values = parse_input_line(input_data)
    assert signal_pattern == expected_signal_pattern
    assert display_values == expected_display_values

