from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def make_point(point_string: str):
    x_str, y_str = point_string.split(',')
    return Point(int(x_str), int(y_str))


class PlumeLine:
    def __init__(self, points: str):
        start_str, end_str = points.split('->')
        self.start = make_point(start_str)
        self.end = make_point(end_str)
