import pytest

from lanternfish import Lanternfish


fish_timer_test_data = [
    (3, 2),
    (1, 0),
    (0, 6),
    (8, 7)
]


@pytest.mark.parametrize("initial_fish_timer_value, expected_next_timer_value", fish_timer_test_data)
def test_fish_timer_progression(initial_fish_timer_value, expected_next_timer_value):
    fish = Lanternfish(initial_fish_timer_value)

    fish.advance_age()
    assert fish.timer == expected_next_timer_value

