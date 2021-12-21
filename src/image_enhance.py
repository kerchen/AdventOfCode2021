from dataclasses import dataclass
from collections import Counter


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int


@dataclass
class ThawedPoint:
    x: int
    y: int


@dataclass
class Rect:
    upper_left: ThawedPoint
    lower_right: ThawedPoint

    def grow(self, pt: Point):
        if self.upper_left.x > pt.x:
            self.upper_left.x = pt.x
        if self.upper_left.y > pt.y:
            self.upper_left.y = pt.y
        if self.lower_right.x < pt.x:
            self.lower_right.x = pt.x
        if self.lower_right.y < pt.y:
            self.lower_right.y = pt.y


def parse_input(input_data: str) -> tuple:
    lines = input_data.split('\n')

    algorithm = lines[0].strip()
    image = lines[2:]

    return algorithm, image


def find_next(start, lit_pixels, keys):
    i = start
    while i < len(keys):
        if lit_pixels[keys[i]]:
            break
        i += 1

    return i


class Image:
    def __init__(self, raw_data: list[str]):
        self.lit_pixels = {}
        self.bounds = Rect(ThawedPoint(100000, 100000), ThawedPoint(-10000, -10000))
        self.infinite_pixels_on = False

        for r, row in enumerate(raw_data):
            for c, pixel_value in enumerate(row):
                pt = Point(c, r)
                self.bounds.grow(pt)
                self.lit_pixels[pt] = (pixel_value == '#')

    def __eq__(self, other):
        if not self.lit_pixels and not other.lit_pixels:
            return True
        if not Counter(self.lit_pixels.values())[True] == Counter(other.lit_pixels.values())[True]:
            return False
        my_keys = sorted(self.lit_pixels)
        my_i = find_next(0, self.lit_pixels, my_keys)
        other_keys = sorted(other.lit_pixels)
        other_i = find_next(0, other.lit_pixels, other_keys)
        dx = my_keys[my_i].x - other_keys[other_i].x
        dy = my_keys[my_i].y - other_keys[other_i].y
        my_i = find_next(my_i+1, self.lit_pixels, my_keys)
        other_i = find_next(other_i+1, other.lit_pixels, other_keys)
        while my_i < len(my_keys):
            if not (my_keys[my_i].x - dx) == other_keys[other_i].x:
                return False
            if not (my_keys[my_i].y - dy) == other_keys[other_i].y:
                return False
            my_i = find_next(my_i+1, self.lit_pixels, my_keys)
            other_i = find_next(other_i+1, other.lit_pixels, other_keys)

        return True

    def dump(self):
        for y in range(self.bounds.upper_left.y, self.bounds.lower_right.y + 1):
            for x in range(self.bounds.upper_left.x, self.bounds.lower_right.x + 1):
                pt = Point(x, y)
                print('#' if self.lit_pixels.get(pt, self.infinite_pixels_on) else '.', end='')
            print('')

    def algorithm_index(self, coordinate: Point) -> int:
        index = 0
        for y in range(coordinate.y-1, coordinate.y+2):
            for x in range(coordinate.x-1, coordinate.x+2):
                index *= 2
                if self.lit_pixels.get(Point(x, y), self.infinite_pixels_on):
                    index += 1

        return index

    def apply_algorithm(self, algorithm: str):
        new_image = Image([])

        for x in range(self.bounds.upper_left.x-2, self.bounds.lower_right.x+3):
            for y in range(self.bounds.upper_left.y-2, self.bounds.lower_right.y+3):
                pt = Point(x, y)
                index = self.algorithm_index(pt)
                new_image.bounds.grow(pt)
                if algorithm[index] == '#':
                    new_image.lit_pixels[pt] = True
                else:
                    new_image.lit_pixels[pt] = False

        if algorithm[0] == '#':
            new_image.infinite_pixels_on = not self.infinite_pixels_on

        return new_image


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        raw_input = dfile.read()
        algorithm, image_data = parse_input(raw_input)
        image = Image(image_data)
        first_gen_image = image.apply_algorithm(algorithm)
        second_gen_image = first_gen_image.apply_algorithm(algorithm)
        print(f"Number of pixels on in second generation: {Counter(second_gen_image.lit_pixels.values())[True]}")
