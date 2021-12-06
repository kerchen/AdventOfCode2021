import pytest

from lanternfish import Lanternfish, simulate_fish


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


fish_spawn_test_data = [
    (3, False),
    (1, False),
    (0, True),
    (8, False)
]


@pytest.mark.parametrize("initial_fish_timer_value, expected_spawn", fish_spawn_test_data)
def test_fish_spawning(initial_fish_timer_value, expected_spawn):
    fish = Lanternfish(initial_fish_timer_value)

    spawn = fish.advance_age()
    assert spawn == expected_spawn


population_progression_test_data = [
    ([3, 1, 5], 1, [2, 0, 4]),
    ([6, 4, 5], 3, [3, 1, 2]),
    ([6, 4, 0], 1, [5, 3, 6, 8])
]


@pytest.mark.parametrize("initial_fish_timer_values, days_to_simulate, expected_timer_values", population_progression_test_data)
def test_fish_population_progression(initial_fish_timer_values, days_to_simulate, expected_timer_values):
    computed_timer_values = simulate_fish(initial_fish_timer_values, days_to_simulate)
    assert computed_timer_values == expected_timer_values
