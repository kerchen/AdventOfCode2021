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


def add_line_coverage(coverage_dict: dict, p: PlumeLine):
    if p.start.x == p.end.x:
        x = p.start.x
        for y in range(min(p.start.y, p.end.y), max(p.start.y, p.end.y)+1):
            coverage_dict[(x, y)] = coverage_dict.get((x, y), 0) + 1
    elif p.start.y == p.end.y:
        y = p.start.y
        for x in range(min(p.start.x, p.end.x), max(p.start.x, p.end.x)+1):
            coverage_dict[(x, y)] = coverage_dict.get((x, y), 0) + 1

    return coverage_dict


class VentField:
    def __init__(self, vent_field_lines: list):
        self.plume_lines = []
        self.line_coverage = dict()
        for f in vent_field_lines:
            p = PlumeLine(f)
            self.plume_lines.append(p)
            self.line_coverage = add_line_coverage(self.line_coverage, p)

    def get_overlap_count(self) -> int:
        if len(self.plume_lines) < 2:
            return 0
        overlapping_cells = list(filter(lambda v: v > 1, self.line_coverage.values()))
        return len(overlapping_cells)


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        vent_lines = []
        for line in dfile:
            vent_lines.append(line.strip())
        field = VentField(vent_lines)
        print(f"Cells with overlapping lines: {field.get_overlap_count()}")
