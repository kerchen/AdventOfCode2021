import pytest

from heightmap import Heightmap


low_point_test_data = [
    (["2199943210",
      "3987894921",
      "9856789892",
      "8767896789",
      "9899965678"], [1, 0, 5, 5]),
    (["30987894921",
      "98567809892",
      "80678960789"], [0, 4, 1, 5, 0, 0, 0]),
    (["309",
      "985",
      "806"], [0, 5, 0]),
    (["3096",
      "9850",
      "8068",
      "4319"], [0, 0, 0, 1]),
    (["9999",
      "8888",
      "7777",
      "6776"], [6, 6]),
]


@pytest.mark.parametrize("input_data, expected_low_points", low_point_test_data)
def test_low_point_calculation(input_data, expected_low_points):
    hm = Heightmap(input_data)

    low_points, _ = hm.find_low_points()
    assert low_points == expected_low_points


low_point_coordinate_test_data = [
    (["2199943210",
      "3987894921",
      "9856789892",
      "8767896789",
      "9899965678"], [(1, 0), (9, 0), (2, 2), (6, 4)]),
    (["30987894921",
      "98567809892",
      "80678960789"], [(1, 0), (7, 0), (10, 0), (2, 1), (6, 1), (1, 2), (7, 2)]),
    (["309",
      "985",
      "806"], [(1, 0), (2, 1), (1, 2)]),
    (["3096",
      "9850",
      "8068",
      "4319"], [(1, 0), (3, 1), (1, 2), (2, 3)]),
    (["9999",
      "8888",
      "7777",
      "6776"], [(0, 3), (3, 3)]),
]


@pytest.mark.parametrize("input_data, expected_low_point_coords", low_point_coordinate_test_data)
def test_low_point_coordinates(input_data, expected_low_point_coords):
    hm = Heightmap(input_data)

    _, coords = hm.find_low_points()
    assert coords == expected_low_point_coords


basin_count_test_data = [
    (["999",
      "909",
      "999"], 1),
    (["30999999921",
      "99967909992",
      "80699990789"], 6),
    (["2199943210",
      "3987894921",
      "9856789892",
      "8767896789",
      "9899965678"], 4),
]


@pytest.mark.parametrize("input_data, expected_basin_count", basin_count_test_data)
def test_basin_count(input_data, expected_basin_count):
    hm = Heightmap(input_data)

    basins = hm.find_basin_sizes()
    assert len(basins) == expected_basin_count


basin_size_test_data = [
    (["999",
      "909",
      "999"], [1]),
    (["99999",
      "90909",
      "99999"], [1, 1]),
    (["999999",
      "909019",
      "999999"], [1, 2]),
    (["9999999",
      "9096019",
      "9999999"], [1, 3]),
    (["9999999",
      "9596519",
      "9096019",
      "9496219",
      "9999999"], [3, 9]),
    (["30999999921",
      "99967909992",
      "80699990789"], [2, 3, 2, 1, 3, 3]),
    (["2199943210",
      "3987894921",
      "9856789892",
      "8767896789",
      "9899965678"], [3, 9, 14, 9]),
]


@pytest.mark.parametrize("input_data, expected_basin_sizes", basin_size_test_data)
def test_basin_sizes(input_data, expected_basin_sizes):
    hm = Heightmap(input_data)

    basins = hm.find_basin_sizes()
    assert basins == expected_basin_sizes
