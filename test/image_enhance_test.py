import pytest

from image_enhance import parse_input, Image, Point, Rect, ThawedPoint


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
    (image_test_data, Point(-1, -1), 0),
    (image_test_data, Point(8, -1), 4),
    (image_test_data, Point(-1, 6), 64),
    (image_test_data, Point(-1, 2), 73),
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
    (['.##',
      '.##'],
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
puzzle_algorithm_str = '########..#..#.##.##.#.#..#.#.###.######.##..##.##..#...#....##.##...##.#.#...#.#.##.###.#.##.#.##.#...#.#.###.#.##.#.####.###..#.####.##..#.#####..####.#.#.#....##.#.#.##...#.####.#....#.##..##...#...#.##..#...#.#..#..#.#.#..##..#.##.##..##...#..###...##..#..###.###.##..#..#####...#.#..###..##....##...#####.#####...##.#.##.#....#.##.#.###.#.##.#.##...######.#...##.#..#.#.#...###.#..#.##.####..##.#..#.##.#.##.######.#.....#.#....####.####.###...#....#..###..###.#...#.#.#.##..#..##.#.#..#..###.#.###..#......'

apply_algorithm_test_data = [
    (puzzle_algorithm_str,
     ['.#.'],
     ['#######',
      '#######',
      '##.####',
      '####.##',
      '#######']),
    (example_algorithm_str,
     ['.#.'],
     ['.##',
      '#.#',
      '.#.']),
    (example_algorithm_str,
     ['...............',
      '...............',
      '.....#..#......',
      '.....#.........',
      '.....##..#.....',
      '.......#.......',
      '.......###.....',
      '...............'],
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
    print(f"\nOriginal image: {image.bounds.upper_left.x}, {image.bounds.upper_left.y}")
    print(f"                {image.bounds.lower_right.x}, {image.bounds.lower_right.y}")
    image.dump()
    print(f"Enhanced image: {enhanced_image.bounds.upper_left.x}, {enhanced_image.bounds.upper_left.y}")
    print(f"                {enhanced_image.bounds.lower_right.x}, {enhanced_image.bounds.lower_right.y}")
    enhanced_image.dump()
    print(f"Expected image: {expected_image.bounds.upper_left.x}, {expected_image.bounds.upper_left.y}")
    print(f"                {expected_image.bounds.lower_right.x}, {expected_image.bounds.lower_right.y}")
    expected_image.dump()
    assert enhanced_image == expected_image


apply_algorithm_twice_test_data = [
    (puzzle_algorithm_str,
     ['.#.'],
     ['...........',
      '....#......',
      '....###....',
      '......#....',
      '...........']),
    ]


@pytest.mark.parametrize('input_algorithm, input_image_data, expected_image_data', apply_algorithm_twice_test_data)
def test_applying_enhancement_twice_algorithm_produces_correct_image(input_algorithm, input_image_data, expected_image_data):
    image = Image(input_image_data)
    expected_image = Image(expected_image_data)
    enhanced_image = image.apply_algorithm(input_algorithm)
    second_enhanced_image = enhanced_image.apply_algorithm(input_algorithm)
    print(f"\nOriginal image: {image.bounds.upper_left.x}, {image.bounds.upper_left.y}")
    print(f"                {image.bounds.lower_right.x}, {image.bounds.lower_right.y}")
    image.dump()
    print(f"Enhanced image: {enhanced_image.bounds.upper_left.x}, {enhanced_image.bounds.upper_left.y}")
    print(f"                {enhanced_image.bounds.lower_right.x}, {enhanced_image.bounds.lower_right.y}")
    enhanced_image.dump()
    print(f"2nd Enh. image: {second_enhanced_image.bounds.upper_left.x}, {second_enhanced_image.bounds.upper_left.y}")
    print(f"                {second_enhanced_image.bounds.lower_right.x}, {second_enhanced_image.bounds.lower_right.y}")
    second_enhanced_image.dump()
    print(f"Expected image: {expected_image.bounds.upper_left.x}, {expected_image.bounds.upper_left.y}")
    print(f"                {expected_image.bounds.lower_right.x}, {expected_image.bounds.lower_right.y}")
    expected_image.dump()
    assert second_enhanced_image == expected_image


bounds_test_data = [
    (['.##',
      '#.#',
      '.#.'],
     Rect(ThawedPoint(0, 0), ThawedPoint(2, 2))
     ),
]


@pytest.mark.parametrize('input_image_data, expected_bounds', bounds_test_data)
def test_bounds_are_set_correctly_upon_image_creation(input_image_data, expected_bounds):
    image = Image(input_image_data)

    assert image.bounds == expected_bounds
