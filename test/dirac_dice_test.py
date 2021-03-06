import pytest
from math import pow

from dirac_dice import DeterministicDie, DiracDiceGame, DiracDie


dice_roll_test_data = [
    (1, 1),
    (7, 7),
    (99, 99),
    (100, 100),
    (101, 1),
    (201, 1),
]


@pytest.mark.parametrize('roll_number, expected_roll', dice_roll_test_data)
def test_deterministic_dice_rolls_expected_value(roll_number, expected_roll):
    dd = DeterministicDie()

    for r in range(roll_number-1):
        dd.roll()

    roll = dd.roll()
    assert roll == expected_roll


score_after_turns_test_data = [
    (1, [2, 3], [8, 8]),
    (1, [9, 1], [5, 6]),
    (2, [6, 4], [8, 11]),
    (5, [6, 4], [30, 25]),
    (6, [6, 4], [32, 29]),
    (9, [6, 4], [54, 51]),
    (15, [6, 4], [90, 80]),
    (16, [6, 4], [92, 84]),
    (17, [6, 4], [98, 91]),
    (18, [6, 4], [106, 99]),
    (27, [6, 4], [158, 146]),
    (4, [4, 8], [26, 22]),
]


@pytest.mark.parametrize('turn_count, starting_positions, expected_scores', score_after_turns_test_data)
def test_game_score_is_correct_after_n_turns(turn_count, starting_positions, expected_scores):
    game = DiracDiceGame(starting_positions)

    game.play_turns(turn_count)
    player1_score = game.score(1)
    player2_score = game.score(2)

    assert player1_score == expected_scores[0]
    assert player2_score == expected_scores[1]


game_ends_at_target_points_test_data = [
    (100, [6, 4], [106, 91]),
    (990, [4, 8], [990, 742]),
    (1000, [4, 8], [1000, 745]),
]


@pytest.mark.parametrize('target_score, starting_positions, expected_scores', game_ends_at_target_points_test_data)
def test_game_ends_at_target_points(target_score, starting_positions, expected_scores):
    game = DiracDiceGame(starting_positions, target_score)

    while True:
        if game.play_turns(1):
            break

    player1_score = game.score(1)
    player2_score = game.score(2)

    assert player1_score == expected_scores[0]
    assert player2_score == expected_scores[1]


dirac_die_test_data = [
    (1, [1, 2, 3]),
    (2, [1, 1, 1, 2, 1, 3, 2, 1, 2, 2, 2, 3, 3, 1, 3, 2, 3, 3]),
    (3, [1, 1, 1, 1, 1, 2, 1, 1, 3,
         1, 2, 1, 1, 2, 2, 1, 2, 3,
         1, 3, 1, 1, 3, 2, 1, 3, 3,
         2, 1, 1, 2, 1, 2, 2, 1, 3,
         2, 2, 1, 2, 2, 2, 2, 2, 3,
         2, 3, 1, 2, 3, 2, 2, 3, 3,
         3, 1, 1, 3, 1, 2, 3, 1, 3,
         3, 2, 1, 3, 2, 2, 3, 2, 3,
         3, 3, 1, 3, 3, 2, 3, 3, 3]),
]


@pytest.mark.parametrize('max_roll_count, expected_sequence', dirac_die_test_data)
def test_dirac_die_returns_correct_sequence(max_roll_count, expected_sequence):
    dd = DiracDie(max_roll_count, 1)

    sequence = []
    for paths in range(int(pow(3, max_roll_count))):
        for i in range(max_roll_count):
            sequence.append(dd.roll(i+1))
        dd.next_universe(max_roll_count)

    assert sequence == expected_sequence


dirac_die_early_out_test_data = [
    (3, 2, [1, 1,
            1, 2,
            1, 3,
            2, 1,
            2, 2,
            2, 3,
            3, 1,
            3, 2,
            3, 3]),
]


@pytest.mark.parametrize('max_roll_count, roll_count, expected_sequence', dirac_die_early_out_test_data)
def test_dirac_die_returns_correct_sequence_when_game_ends_early(max_roll_count, roll_count, expected_sequence):
    dd = DiracDie(max_roll_count, 1)

    sequence = []
    for paths in range(int(pow(3, max_roll_count))):
        for i in range(roll_count):
            sequence.append(dd.roll(i+1))
        dd.next_universe(roll_count)
        if dd.is_exhausted():
            break

    print("\nComputed vs expected:")
    print(sequence)
    print(expected_sequence)
    assert sequence == expected_sequence
