
def make_cells(numbers: list) -> list:
    return_list = []
    for row in numbers:
        return_list.append(list(map(int, row.split())))
    return return_list


class BingoBoard:
    def __init__(self, board_numbers: list):
        self.cells = make_cells(board_numbers)
        self.board_size = len(self.cells)
        self.called_numbers = []

    def call_numbers(self, numbers: str):
        self.called_numbers.extend(map(int, numbers.split(',')))

    def find_number(self, number: int) -> tuple:
        for row, columns in enumerate(self.cells):
            for column, value in enumerate(columns):
                if number == value:
                    return row, column

        return -1, -1

    def get_winning_numbers(self) -> tuple:
        winning_number = -1
        score = 0
        if len(self.called_numbers) < self.board_size:
            return winning_number, score

        row_marks = [[False for i in range(self.board_size)] for j in range(self.board_size)]
        column_marks = [[False for i in range(self.board_size)] for j in range(self.board_size)]
        for n in self.called_numbers:
            row, column = self.find_number(n)
            if row < 0 or column < 0:
                continue
            row_marks[row][column] = True
            column_marks[column][row] = True
            if all(row_marks[row]):
                winning_number = n
                break
            if all(column_marks[column]):
                winning_number = n
                break

        for i, columns in enumerate(row_marks):
            for j, mark in enumerate(columns):
                if not mark:
                    score += self.cells[i][j]

        return winning_number, score

    def has_bingo(self):
        winning_number, score = self.get_winning_numbers()
        return winning_number > -1

