import pytest

from bingo_player import BingoPlayer

test_board_numbers = [
    " 1  2  3  4  5",
    " 6  7  8  9 10",
    "11 12 13 14 15",
    "16 17 18 19 20",
    "21 22 23 24 25"
]

player_board_count_test_data = [
    ([test_board_numbers],
     1),
    ([test_board_numbers,
      test_board_numbers,
      test_board_numbers],
     3),
]


@pytest.mark.parametrize("board_numbers, expected_board_count", player_board_count_test_data)
def test_player_board_count(board_numbers, expected_board_count):
    player = BingoPlayer(board_numbers)

    assert len(player.boards) == expected_board_count


example_test_data = [
    ([["22 13 17 11  0",
       "8  2 23  4 24",
       "21  9 14 16  7",
       "6 10  3 18  5",
       "1 12 20 15 19"],

      ["3 15  0  2 22",
       "9 18 13 17  5",
       "19  8  7 25 23",
       "20 11 10 24  4",
       "14 21 16 12  6"],

      ["14 21 17 24  4",
       "10 16 15  9 19",
       "18  8 23 26 20",
       "22 11 13  6  5",
       "2  0 12  3  7"]],
     "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
     2
     )
]


@pytest.mark.parametrize("board_numbers, called_numbers, expected_winning_board", example_test_data)
def test_first_winning_board(board_numbers, called_numbers, expected_winning_board):
    player = BingoPlayer(board_numbers)

    first, _ = player.play_boards(called_numbers)
    assert first == expected_winning_board


example_last_winning_test_data = [
    ([["22 13 17 11  0",
       "8  2 23  4 24",
       "21  9 14 16  7",
       "6 10  3 18  5",
       "1 12 20 15 19"],

      ["3 15  0  2 22",
       "9 18 13 17  5",
       "19  8  7 25 23",
       "20 11 10 24  4",
       "14 21 16 12  6"],

      ["14 21 17 24  4",
       "10 16 15  9 19",
       "18  8 23 26 20",
       "22 11 13  6  5",
       "2  0 12  3  7"]],
     "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
     1
     )
]


@pytest.mark.parametrize("board_numbers, called_numbers, expected_last_winning_board", example_last_winning_test_data)
def test_last_winning_board(board_numbers, called_numbers, expected_last_winning_board):
    player = BingoPlayer(board_numbers)

    _, last = player.play_boards(called_numbers)
    assert last == expected_last_winning_board
