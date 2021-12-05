import pytest

from bingo import make_cells, BingoBoard

test_board_numbers = [
    " 1  2  3  4  5",
    " 6  7  8  9 10",
    "11 12 13 14 15",
    "16 17 18 19 20",
    "21 22 23 24 25"
]


def test_cells_creation():
    cells = make_cells(test_board_numbers)
    assert cells == [[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]]


find_numbers_test_data = [
    (test_board_numbers,
     1,
     (0, 0)),
    (test_board_numbers,
     2,
     (0, 1)),
    (test_board_numbers,
     6,
     (1, 0)),
    (test_board_numbers,
     19,
     (3, 3)),
    (test_board_numbers,
     25,
     (4, 4)),
    (test_board_numbers,
     33,
     (-1, -1)),
]


@pytest.mark.parametrize("board_numbers, number_to_find, expected_cell", find_numbers_test_data)
def test_find_numbers(board_numbers, number_to_find, expected_cell):
    board = BingoBoard(board_numbers)

    found_cell = board.find_number(number_to_find)
    assert found_cell == expected_cell


board_win_test_data = [
    (test_board_numbers,
     "21",
     False),
    (test_board_numbers,
     "21, 22, 23, 24, 25",
     True),
    (test_board_numbers,
     "21, 22, 23, 24, 25, 26",
     True),
    (test_board_numbers,
     "3, 8, 13, 18, 23",
     True),
    (test_board_numbers,
     "2, 8, 13, 18, 23",
     False),
    (test_board_numbers,
     "5, 9, 13, 17, 21, 25, 3, 8, 18, 23, 15, 22",
     True),
]


@pytest.mark.parametrize("board_numbers, called_numbers, expected_bingo", board_win_test_data)
def test_board_win(board_numbers, called_numbers, expected_bingo):
    board = BingoBoard(board_numbers)

    board.call_numbers(called_numbers)

    assert board.has_bingo() == expected_bingo


winning_number_test_data = [
    (test_board_numbers,
     "21",
     -1),
    (test_board_numbers,
     "21, 22, 23, 24, 25",
     25),
    (test_board_numbers,
     "21, 22, 23, 24, 25, 26",
     25),
    (test_board_numbers,
     "5, 9, 13, 17, 21, 25, 3, 8, 18, 23, 15, 22",
     23),
]


@pytest.mark.parametrize("board_numbers, called_numbers, expected_winning_number", winning_number_test_data)
def test_winning_number(board_numbers, called_numbers, expected_winning_number):
    board = BingoBoard(board_numbers)

    board.call_numbers(called_numbers)
    winning_number, _ = board.get_winning_numbers()
    assert winning_number == expected_winning_number


winning_score_test_data = [
    (test_board_numbers,
     "21",
     0),
    (test_board_numbers,
     "21, 22, 23, 24, 25",
     210),
    (test_board_numbers,
     "21, 22, 23, 24, 25, 26",
     210),
    (test_board_numbers,
     "5, 9, 13, 17, 21, 25, 3, 8, 18, 23, 15, 22",
     63),
]


@pytest.mark.parametrize("board_numbers, called_numbers, expected_winning_number", winning_number_test_data)
def test_winning_number(board_numbers, called_numbers, expected_winning_number):
    board = BingoBoard(board_numbers)

    board.call_numbers(called_numbers)
    winning_number, _ = board.get_winning_numbers()
    assert winning_number == expected_winning_number
