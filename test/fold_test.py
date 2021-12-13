import pytest

from fold import Point, parse_instructions, Paper


dot_parse_test_data = [
    ('''1,1
7,2
3,9
4,5

fold along x=1
fold along y=3''',
     [Point(1, 1), Point(7, 2), Point(3, 9), Point(4, 5)]
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


fold_test_data = [
    ('''1,0
4,5
''',
     [Point(1, 0), Point(4, 5)]
     ),
    ('''1,0
4,5

fold along y=3''',
     [Point(1, 0), Point(4, 1)]
     ),
    ('''1,0
1,6

fold along y=3''',
     [Point(1, 0)]
     ),
    ('''1,0
4,1

fold along x=3''',
     [Point(1, 0), Point(0, 1)]
     ),
    ('''8,0
0,1
6,2
0,4
10,4
3,5

fold along x=5''',
     [Point(2, 0), Point(4, 1), Point(0, 2), Point(4, 4), Point(1, 5)]
     ),
    ('''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7''',
     [Point(0, 0), Point(2, 0), Point(3, 0), Point(6, 0), Point(9, 0),
      Point(0, 1), Point(4, 1),
      Point(6, 2), Point(10, 2),
      Point(0, 3), Point(4, 3),
      Point(1, 4), Point(3, 4), Point(6, 4), Point(8, 4), Point(9, 4), Point(10, 4)]),
    (
'''0, 0
2, 0
3, 0
6, 0
9, 0
0, 1
4, 1
6, 2
10, 2
0, 3
4, 3
1, 4
3, 4
6, 4
8, 4
9, 4
10, 4

fold along x=5''',
        [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(4, 0),
         Point(0, 1), Point(4, 1),
         Point(0, 2), Point(4, 2),
         Point(0, 3), Point(4, 3),
         Point(0, 4), Point(1, 4), Point(2, 4), Point(3, 4), Point(4, 4)]
    ),
]


@pytest.mark.parametrize("input_data, expected_dot_coords", fold_test_data)
def test_folding_results_in_correct_dots(input_data, expected_dot_coords):
    dots, folds = parse_instructions(input_data)
    paper = Paper(dots)
    expected_paper = Paper(expected_dot_coords)
    paper.fold(folds)

    assert paper == expected_paper
