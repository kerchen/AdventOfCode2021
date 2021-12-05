from dataclasses import dataclass


@dataclass
class Point:
     x: int
     y: int


class PlumeLine:
    def __init__(self, points: str):
        start_str, end_str = points.split('->')

        self.start = Point()