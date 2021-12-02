import pytest

from aimed_submarine import AimedSubmarine


position_test_data = [
    (["forward 1"], 1),
    (["forward 11"], 11)
]


@pytest.mark.parametrize("movement_commands, expected_position", position_test_data)
def test_position_commands_result_in_correct_position(movement_commands, expected_position):
    boat = AimedSubmarine()

    boat.move(movement_commands)
    assert boat.position == expected_position


aim_test_data = [
    (["forward 1"], 0),
    (["forward 11"], 0),
    (["down 4"], 4),
    (["up 8"], -8),
    (["down 3",
      "up 1",
      "down 4",
      "up 2"], 4),
]


@pytest.mark.parametrize("movement_commands, expected_aim", aim_test_data)
def test_aim_commands_result_in_correct_aim(movement_commands, expected_aim):
    boat = AimedSubmarine()

    boat.move(movement_commands)
    assert boat.aim == expected_aim


aim_depth_test_data = [
    (["forward 1"], 0),
    (["down 6"], 0),
    (["down 3",
      "forward 7"], 21),
    (["down 3",
      "forward 1",
      "up 1",
      "forward 4"], 11),
    (["forward 5",
      "down 5",
      "forward 8",
      "up 3",
      "down 8",
      "forward 2"], 60)
]


@pytest.mark.parametrize("movement_commands, expected_depth", aim_depth_test_data)
def test_aim_plus_forward_commands_result_in_correct_dept(movement_commands, expected_depth):
    boat = AimedSubmarine()

    boat.move(movement_commands)
    assert boat.depth == expected_depth
