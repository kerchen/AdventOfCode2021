import pytest

from syntax import is_corrupt, get_corruption_score, complete_line, compute_completion_score


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


completion_test_data = [
    ("(", ")"),
    ("<", ">"),
    ("{<>", "}"),
    ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
    ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
    ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
    ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
    ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>")
]


@pytest.mark.parametrize("input_line, expected_completion", completion_test_data)
def test_completion_matches_unmatched_delimiters(input_line, expected_completion):
    completion = complete_line(input_line)
    assert completion == expected_completion


completion_score_test_data = [
    (")", 1),
    (">", 4),
    ("}", 3),
    ("}}", 18),
    (")>}]", 242),
    ("}}]])})]", 288957),
    (")}>]})", 5566),
    ("}}>}>))))", 1480781),
    ("]]}}]}]}>", 995444),
    ("])}>", 294)
]


@pytest.mark.parametrize("input_line, expected_score", completion_score_test_data)
def test_completion_score_is_computed_correctly(input_line, expected_score):
    score = compute_completion_score(input_line)
    assert score == expected_score

