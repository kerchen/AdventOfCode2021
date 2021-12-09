
class Heightmap:
    def __init__(self, heights: list):
        self.heightmap = dict()
        self.row_count = len(heights)
        self.col_count = 0
        for r, row in enumerate(heights):
            self.col_count = len(row)
            for c, h in enumerate(row):
                self.heightmap[(c, r)] = int(h)
        print(f"Row count: {self.row_count}\nCol count: {self.col_count}")

    def is_lower_than_neighbors(self, c, r):
        max_height = 10
        height = self.heightmap.get((c, r))
        if self.heightmap.get((c, r - 1), max_height) <= height:
            return False
        if self.heightmap.get((c, r + 1), max_height) <= height:
            return False
        if self.heightmap.get((c - 1, r), max_height) <= height:
            return False
        if self.heightmap.get((c + 1, r), max_height) <= height:
            return False

        return True

    def find_low_points(self):
        low_points = []
        for r in range(self.row_count):
            for c in range(self.col_count):
                if self.is_lower_than_neighbors(c, r):
                    low_points.append(self.heightmap.get((c, r)))

        return low_points

    def compute_risk_level(self):
        low_points = self.find_low_points()
        return sum(low_points) + len(low_points)


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        height_data = []
        for line in dfile:
            height_data.append(line.strip())

        hm = Heightmap(height_data)
        print(f"Risk level: {hm.compute_risk_level()}")
