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

    low_points = hm.find_low_points()
    assert low_points == expected_low_points
