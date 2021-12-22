import pytest

from riskmap import Riskmap

low_path_test_data = [
    ('''1234
1344
1344''', 3),
    ('''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581''', 40),
]


@pytest.mark.parametrize("input_data, expected_lowest_risk", low_path_test_data)
def test_lowest_risk_path_is_found(input_data, expected_lowest_risk):
    rm = Riskmap(input_data)

    lowest_risk = rm.find_lowest_risk(0, 0)
    assert lowest_risk == expected_lowest_risk

