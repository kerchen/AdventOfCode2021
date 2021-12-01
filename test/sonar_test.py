import pytest

import sonar


increase_count_test_data = [
    ([], 0),
    ([1], 0),
    ([1, 1], 0),
    ([1, 2], 1),
    ([1, 2, 3, 4, 5], 4),
    ([1, 2, 2, 1, 5], 2),
    ([5, 4, 3, 2, 1, 0], 0),
    ([1, 1, 1, 1, 1], 0)
]


@pytest.mark.parametrize("depth_readings, expected_increase", increase_count_test_data)
def test_number_of_increases_is_correct(depth_readings, expected_increase):
    stats = sonar.get_depth_stats(depth_readings)

    assert(stats.increase_count == expected_increase)


sliding_window_count_test_data = [
    ([], 0),
    ([1], 0),
    ([1, 1], 0),
    ([1, 2], 0),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7),
    ([1, 2, 3, 4, 5, 1, 1, 19, 20, 1], 4),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0),
]


@pytest.mark.parametrize("depth_readings, expected_increase", sliding_window_count_test_data)
def test_number_of_increases_is_correct_with_sliding_window(depth_readings, expected_increase):
    stats = sonar.get_depth_stats(depth_readings, 3)

    assert(stats.increase_count == expected_increase)
