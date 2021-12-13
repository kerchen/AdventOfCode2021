import pytest

from fold import parse_instructions


dot_parse_test_data = [
    ('''1,1
7,2
3,9

fold along x=1
fold along y=3''',
     [(1, 1), (7, 2), (3, 9)]
     ),
]


@pytest.mark.parametrize("input_data, expected_dot_coords", dot_parse_test_data)
def test_input_dot_data_parsed_correctly(input_data, expected_dot_coords):
    dots, _ = parse_instructions(input_data)
    assert dots == expected_dot_coords


fold_parse_test_data = [
    ('''1,1

fold along x=1
fold along y=397
fold along x=7
fold along y=3''',
     [('x', 1), ('y', 397), ('x', 7), ('y', 3)]),
]


@pytest.mark.parametrize("input_data, expected_fold_instructions", fold_parse_test_data)
def test_input_fold_data_parsed_correctly(input_data, expected_fold_instructions):
    _, folds = parse_instructions(input_data)
    assert folds == expected_fold_instructions

