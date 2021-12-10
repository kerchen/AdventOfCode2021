import pytest

from syntax import is_corrupt, get_corruption_score


corrupt_line_test_data = [
    ("<>", False),
    ("[]", False),
    ("{}", False),
    ("()", False),
    ("", False),
    ("<hi>", False),
    (">", True),
    ("(>", True),
    ("( {}()>", True),
    ("(", False),  # Incomplete but not corrupted
    ("(<?>){[][][]}<<{([])}>>", False),
    ("[({(<(())[]>[[{[]{<()<>>", False),
    ("[(()[<>])]({[<{<<[]>>(", False),
    ("{([(<{}[<>[]}>{[]{[(<()>", True),
    ("(((({<>}<{<{<>}{[]{[]{}", False),
    ("[[<[([]))<([[{}[[()]]]", True),
    ("[{[{({}]{}}([{[{{{}}([]", True),
    ("{<[[]]>}<{[{[{[]{()[[[]", False),
    ("[<(<(<(<{}))><([]([]()", True),
    ("<{([([[(<>()){}]>(<<{{", True),
    ("<{([{{}}[<[[[<>{}]]]>[]]", False)
]


@pytest.mark.parametrize("input_line, expected_corrupt", corrupt_line_test_data)
def test_corrupt_line_detection(input_line, expected_corrupt):
    corrupt, _ = is_corrupt(input_line)
    assert corrupt == expected_corrupt


corrupt_line_score_test_data = [
    (">", 25137),
    ("{)", 3),
    ("( {}()]", 57),
    ("}", 1197),
    ("{([(<{}[<>[]}>{[]{[(<()>", 1197),
    ("[[<[([]))<([[{}[[()]]]", 3),
    ("[{[{({}]{}}([{[{{{}}([]", 57),
    ("[<(<(<(<{}))><([]([]()", 3),
    ("<{([([[(<>()){}]>(<<{{", 25137),
]


@pytest.mark.parametrize("input_line, expected_score", corrupt_line_score_test_data)
def test_corrupt_line_score_is_correct(input_line, expected_score):
    corrupt, stop_char = is_corrupt(input_line)
    score = get_corruption_score(stop_char)
    assert score == expected_score
