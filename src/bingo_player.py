from bingo import BingoBoard


class BingoPlayer:
    def __init__(self, boards: list):
        self.boards = []
        for b in boards:
            self.boards.append(BingoBoard(b))

    def play_boards(self, called_numbers: str) -> tuple:
        first_winning_board = -1
        last_winning_board = -1
        already_won = set()
        for n in called_numbers.split(','):
            for i, b in enumerate(self.boards):
                if i not in already_won:
                    b.call_numbers(n)
                    if b.has_bingo():
                        already_won.add(i)
                        if first_winning_board == -1:
                            first_winning_board = i
                            winning_number, score = b.get_winning_numbers()
                            print(f"Winning board is {i} with winning number {winning_number} and score {score}")
                            winning_number = 0
                            score = 0
                        else:
                            last_winning_board = i
                            winning_number, score = b.get_winning_numbers()

        print(f"Last winning board is {last_winning_board} with winning number {winning_number} and score {score}")

        return first_winning_board, last_winning_board


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        called_numbers = None
        board_data = []
        boards = []
        for line in dfile:
            stripped_line = line.strip()
            if not called_numbers:
                called_numbers = stripped_line
                continue
            if not stripped_line:
                if board_data:
                    boards.append(board_data)
                    board_data = []
                continue
            board_data.append(stripped_line)

        if board_data:
            boards.append(board_data)

        player = BingoPlayer(boards)
        player.play_boards(called_numbers)
