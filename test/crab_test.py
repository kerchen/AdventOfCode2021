import pytest

from crab import find_best_meeting_point, geometric_cost


crab_meet_position_test_data = [
    ([1], 1),
    ([1, 4], 2),
    ([1, 1, 4], 1),
    ([0, 0, 400], 0),
    ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2)
]


@pytest.mark.parametrize("crab_locations, expected_best_position", crab_meet_position_test_data)
def test_crabs_meet_at_best_position(crab_locations, expected_best_position):
    meeting_point, _ = find_best_meeting_point(crab_locations)
    assert meeting_point == expected_best_position


crab_meet_cost_test_data = [
    ([1], 0),
    ([1, 4], 3),
    ([1, 1, 4], 3),
    ([0, 0, 400], 400),
    ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 37)
]


@pytest.mark.parametrize("crab_locations, expected_best_cost", crab_meet_cost_test_data)
def test_crabs_meet_at_best_cost(crab_locations, expected_best_cost):
    _, meeting_cost = find_best_meeting_point(crab_locations)
    assert meeting_cost == expected_best_cost


geometric_cost_test_data = [
    (1, 1, 0),
    (1, 2, 1),
    (1, 3, 3),
    (1, 4, 6),
    (1, 5, 10),
]


@pytest.mark.parametrize("pos, target, expected_cost", geometric_cost_test_data)
def test_geometric_cost_is_correct(pos, target, expected_cost):
    cost = geometric_cost(pos, target)
    assert cost == expected_cost


crab_position_geometric_cost_test_data = [
    ([1], 1),
    ([1, 4], 2),
    ([1, 1, 4], 2),
    ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 5)
]


@pytest.mark.parametrize("crab_locations, expected_best_position", crab_position_geometric_cost_test_data)
def test_crabs_meet_at_best_position_for_geometric_cost(crab_locations, expected_best_position):
    meeting_point, _ = find_best_meeting_point(crab_locations, geometric_cost)
    assert meeting_point == expected_best_position


crab_geometric_cost_test_data = [
    ([1], 0),
    ([1, 4], 4),
    ([1, 1, 4], 5),
    ([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 168)
]


@pytest.mark.parametrize("crab_locations, expected_best_cost", crab_geometric_cost_test_data)
def test_crabs_meet_at_best_geometric_cost(crab_locations, expected_best_cost):
    _, meeting_cost = find_best_meeting_point(crab_locations, geometric_cost)
    assert meeting_cost == expected_best_cost
