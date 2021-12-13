from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def make_point(point_string: str):
    x_str, y_str = point_string.split(',')
    return Point(int(x_str), int(y_str))


def parse_instructions(input_data: str) -> tuple:
    dots = []
    folds = []

    for line in input_data.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('fold along '):
            fold_data = line[11:].split('=')
            folds.append((fold_data[0], int(fold_data[1])))
        else:
            dots.append(make_point(line))

    return dots, folds


def print_state(paper):
    max_col = 0
    max_row = 0
    for k in paper.page.keys():
        if k.x > max_col:
            max_col = k.x
        if k.y > max_row:
            max_row = k.y

    for y in range(max_row+1):
        for x in range(max_col, -1, -1):
            print('*' if paper.page.get(Point(x, y), False) else ' ', end='')
        print('')


class Paper:
    def __init__(self, dot_coords: list):
        self.page = dict()
        for dot in dot_coords:
            self.page[dot] = True

    def __eq__(self, other):
        if not isinstance(other, Paper):
            return NotImplemented

        return self.page == other.page

    def fold(self, fold_instructions: list):
        if not fold_instructions:
            return

        for fold in fold_instructions:
            if fold[0] == 'y':
                self.fold_along_y(fold[1])
            elif fold[0] == 'x':
                self.fold_along_x(fold[1])

    def fold_along_y(self, coord):
        for dot in list(self.page.keys()):
            if dot.y < coord:
                continue
            del self.page[dot]
            new_dot = Point(dot.x, dot.y - 2*(dot.y - coord))
            self.page[new_dot] = True

    def fold_along_x(self, coord):
        new_dots = set()
        for dot in list(self.page.keys()):
            if dot not in new_dots:
                del self.page[dot]
            if dot.x > coord:
                new_dot = Point(dot.x - coord - 1, dot.y)
            else:
                new_dot = Point(coord - dot.x - 1, dot.y)
            self.page[new_dot] = True
            new_dots.add(new_dot)

'''
    def fold_along_x(self, coord):
        for dot in list(self.page.keys()):
            if dot.x < coord:
                continue
            del self.page[dot]
            new_dot = Point(dot.x - 2*(dot.x - coord), dot.y)
            self.page[new_dot] = True
'''
def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        dots, folds = parse_instructions(dfile.read())

        paper = Paper(dots)
        print(f"Visible dots before any folding: {len(paper.page)}")
        paper.fold(folds[:1])
        print(f"Visible dots after one fold: {len(paper.page)}")

        paper.fold(folds[1:])
        print("Camera code:")
        print_state(paper)
