from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def parse_input(input_data: str) -> tuple:
    lines = input_data.split('\n')

    algorithm = lines[0].strip()
    image = lines[2:]

    return algorithm, image


class Image:
    def __init__(self, raw_data: list[str]):
        self.lit_pixels = {}
        for r, row in enumerate(raw_data):
            for c, pixel_value in enumerate(row):
                if pixel_value == '#':
                    self.lit_pixels[Point(c, r)] = True

    def algorithm_index(self, coordinate: Point) -> int:
        index = 0
        for y in range(coordinate.y-1, coordinate.y+2):
            for x in range(coordinate.x-1, coordinate.x+2):
                index *= 2
                if self.lit_pixels.get(Point(x, y), False):
                    index += 1

        return index
