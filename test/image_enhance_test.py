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


image_equality_test_data = [
    ([], [], True),
    ([], ['#'], False),
    (['#'], ['#'], True),
    (['.##'], ['#'], False),
    (['.##',
      '##.'],
     ['##.',
      '.##'],
     False),
    (['.#.',
      '##.',
      '#.#'],
     ['......',
      '..#...',
      '.##...',
      '.#.#..',
      '.....'],
     True)
]


@pytest.mark.parametrize('input_image1, input_image2, expected_equal', image_equality_test_data)
def test_image_equality_is_correct(input_image1, input_image2, expected_equal):
    image1 = Image(input_image1)
    image2 = Image(input_image2)

    if expected_equal:
        assert image1 == image2
    else:
        assert not image1 == image2

example_algorithm_str = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'

apply_algorithm_test_data = [
    (example_algorithm_str,
     ['.#.'],
     ['.##',
      '#.#',
      '.#.']),
    (example_algorithm_str,
     ['...............',
      '.....#..#......',
      '.....#.........',
      '.....##..#.....',
      '.......#.......',
      '.......###.....'],
     ['...............',
      '...............',
      '...............',
      '...............',
      '.....##.##.....',
      '....#..#.#.....',
      '....##.#..#....',
      '....####..#....',
      '.....#..##.....',
      '......##..#....',
      '.......#.#.....',
      '...............',
      '...............',
      '...............',
      '...............']
     ),
    (example_algorithm_str,
     ['...............',
      '...............',
      '...............',
      '...............',
      '.....##.##.....',
      '....#..#.#.....',
      '....##.#..#....',
      '....####..#....',
      '.....#..##.....',
      '......##..#....',
      '.......#.#.....',
      '...............',
      '...............',
      '...............',
      '...............'],
     ['...............',
      '..........#....',
      '....#..#.#.....',
      '...#.#...###...',
      '...#...##.#....',
      '...#.....#.#...',
      '....#.#####....',
      '.....#.#####...',
      '......##.##....',
      '.......###.....',
      '...............'])
]


@pytest.mark.parametrize('input_algorithm, input_image_data, expected_image_data', apply_algorithm_test_data)
def test_applying_enhancement_algorithm_produces_correct_image(input_algorithm, input_image_data, expected_image_data):
    image = Image(input_image_data)
    expected_image = Image(expected_image_data)
    enhanced_image = image.apply_algorithm(input_algorithm)
    assert enhanced_image == expected_image
