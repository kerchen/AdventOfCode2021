import pytest

from segment_display import parse_input_line, deduce_a, deduce_bd, deduce_eg, deduce_digits


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


a_deduction_test_data = [
    ("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe", set(['d'])),
    ("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", set(['b'])),
    ("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg", set(['b'])),
    ("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb", set(['d'])),
    ("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea", set(['b'])),
    ("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", set(['f'])),
    ("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", set(['d'])),
    ("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", set(['c'])),
    ("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb", set(['b'])),
    ("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce", set(['c'])),
]


@pytest.mark.parametrize("input_data, expected_deduced_a", a_deduction_test_data)
def test_a_deduction(input_data, expected_deduced_a):
    signal_pattern, _ = parse_input_line(input_data)
    deduced_a = deduce_a(signal_pattern)
    assert deduced_a == expected_deduced_a

bd_deduction_test_data = [
    ("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe", set(['c', 'g'])),
    ("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", set(['e', 'f'])),
    ("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",  set(['a', 'f'])),
    ("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb", set(['a', 'f'])),
    ("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea", set(['c', 'e'])),
    ("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", set(['b', 'e'])),
    ("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", set(['c', 'e'])),
    ("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", set(['b', 'f'])),
    ("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb", set(['d', 'e'])),
    ("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce", set(['a', 'e'])),
]


@pytest.mark.parametrize("input_data, expected_deduced_bd", bd_deduction_test_data)
def test_bd_deduction(input_data, expected_deduced_bd):
    signal_pattern, _ = parse_input_line(input_data)
    deduced_bd = deduce_bd(signal_pattern)
    assert deduced_bd == expected_deduced_bd


eg_deduction_test_data = [
    ("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe", set(['a', 'f'])),
    ("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", set(['a', 'd'])),
    ("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",  set(['d', 'e'])),
    ("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb", set(['e', 'g'])),
    ("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea", set(['a', 'd'])),
    ("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", set(['d', 'g'])),
    ("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", set(['a', 'b'])),
    ("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", set(['a', 'g'])),
    ("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb", set(['a', 'f'])),
    ("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce", set(['b', 'd'])),
]


@pytest.mark.parametrize("input_data, expected_deduced_eg", eg_deduction_test_data)
def test_eg_deduction(input_data, expected_deduced_eg):
    signal_pattern, _ = parse_input_line(input_data)
    deduced_eg = deduce_eg(signal_pattern)
    assert deduced_eg == expected_deduced_eg


final_deduction_test_data = [
    ("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe", 8394),
    ("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", 9781),
    ("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg", 1197),
    ("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb", 9361),
    ("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea", 4873),
    ("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", 8418),
    ("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", 4548),
    ("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", 1625),
    ("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb", 8717),
    ("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce", 4315),
]


@pytest.mark.parametrize("input_data, expected_deduced_digits", final_deduction_test_data)
def test_final_deduction(input_data, expected_deduced_digits):
    signal_pattern, display_digits = parse_input_line(input_data)
    deduced_digits = deduce_digits(signal_pattern, display_digits)
    assert deduced_digits == expected_deduced_digits

