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
