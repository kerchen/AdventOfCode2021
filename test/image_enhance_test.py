import pytest

from image_enhance import parse_input, Image, Point


image_test_data = [
    '.#...#.#',
    '#..###..',
    '#...####',
    '######..',
    '.....#..',
    '#..#....'
]

parser_test_data = [
    ('''.#..#..###.#..##.#.#...#...#

.#...#.#
#..###..
#...####
######..
.....#..
#..#....''',
     '.#..#..###.#..##.#.#...#...#',
     image_test_data)
]


@pytest.mark.parametrize('input_data, expected_algorithm, expected_image', parser_test_data)
def test_input_parser(input_data, expected_algorithm, expected_image):
    algorithm, image = parse_input(input_data)

    assert algorithm == expected_algorithm
    assert image == expected_image


image_coordinate_index_computation_test_data = [
    (image_test_data, Point(0, 0), 10),
    (image_test_data, Point(4, 1), 123),
    (image_test_data, Point(1, 4), 452),
]


@pytest.mark.parametrize('input_image, coordinate, expected_index', image_coordinate_index_computation_test_data)
def test_coordinate_to_index_computation_is_correct(input_image, coordinate, expected_index):
    image = Image(input_image)
    index = image.algorithm_index(coordinate)

    assert index == expected_index
