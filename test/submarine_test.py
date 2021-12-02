import pytest

from submarine import Submarine

position_test_data = [
    (["forward 1"], 1),
    (["forward 7"], 7),
    (["forward 7",
      "forward 2"], 9),
    (["forward 2",
      "forward 6",
      "down 7",
      "forward 1",
      "forward 33"], 42)
]


@pytest.mark.parametrize("movement_commands, expected_position", position_test_data)
def test_forward_movements_result_in_correct_position(movement_commands, expected_position):
    boat = Submarine()

    boat.move(movement_commands)
    assert boat.position == expected_position


depth_test_data = [
    (["down 1"], 1),
    (["down 3"], 3),
    (["down 3",
      "down 1",
      "down 8"], 12),
    (["up 1"], -1),  # You can fly!
    (["down 3",
      "up 1",
      "down 8",
      "up 3"], 7),
]


@pytest.mark.parametrize("movement_commands, expected_depth", depth_test_data)
def test_depth_commands_result_in_correct_depth(movement_commands, expected_depth):
    boat = Submarine()

    boat.move(movement_commands)
    assert boat.depth == expected_depth


