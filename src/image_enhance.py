from dataclasses import dataclass


@dataclass(frozen=True, order=True)
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

    def __eq__(self, other):
        if not self.lit_pixels and not other.lit_pixels:
            return True
        if not len(self.lit_pixels) == len(other.lit_pixels):
            return False
        my_pixels = sorted(self.lit_pixels)
        other_pixels = sorted(other.lit_pixels)
        dx = my_pixels[0].x - other_pixels[0].x
        dy = my_pixels[0].y - other_pixels[0].y
        for i in range(len(my_pixels)):
            if not (my_pixels[i].x - dx) == other_pixels[i].x:
                return False
            if not (my_pixels[i].y - dy) == other_pixels[i].y:
                return False

        return True

    def algorithm_index(self, coordinate: Point) -> int:
        index = 0
        for y in range(coordinate.y-1, coordinate.y+2):
            for x in range(coordinate.x-1, coordinate.x+2):
                index *= 2
                if self.lit_pixels.get(Point(x, y), False):
                    index += 1

        return index

    def apply_algorithm(self, algorithm: str):
        new_image = Image([])
        already_computed = set()

        for k in sorted(self.lit_pixels):
            for y in range(k.y-1, k.y+2):
                for x in range(k.x-1, k.x+2):
                    pt = Point(x, y)
                    if pt not in already_computed:
                        already_computed.add(pt)
                        index = self.algorithm_index(pt)
                        if algorithm[index] == '#':
                            new_image.lit_pixels[pt] = True

        return new_image


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        raw_input = dfile.read()
        algorithm, image_data = parse_input(raw_input)
        image = Image(image_data)
        print(f"Number of pixels in original image: {len(image.lit_pixels)}")
        first_gen_image = image.apply_algorithm(algorithm)
        print(f"Number of pixels in first generation: {len(first_gen_image.lit_pixels)}")
        second_gen_image = first_gen_image.apply_algorithm(algorithm)

        print(f"Number of pixels on in second generation: {len(second_gen_image.lit_pixels)}")
