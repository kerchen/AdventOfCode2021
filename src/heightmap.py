
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

    def is_lower_than_neighbors(self, c, r) -> bool:
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

    def find_low_points(self) -> list:
        low_points = []
        low_point_coords = []
        for r in range(self.row_count):
            for c in range(self.col_count):
                if self.is_lower_than_neighbors(c, r):
                    low_points.append(self.heightmap.get((c, r)))
                    low_point_coords.append((c, r))

        return low_points, low_point_coords

    def compute_risk_level(self) -> int:
        low_points, _ = self.find_low_points()
        return sum(low_points) + len(low_points)

    def add_to_basin(self, members, possible_member):
        if possible_member in members:
            return members

        edge_height = 9
        if self.heightmap.get(possible_member, edge_height) < edge_height:
            members.add(possible_member)
            members = self.grow_basin(members, possible_member)
        return members

    def grow_basin(self, members, from_point):
        members.add(from_point)
        members = self.add_to_basin(members, (from_point[0] + 1, from_point[1]))
        members = self.add_to_basin(members, (from_point[0] - 1, from_point[1]))
        members = self.add_to_basin(members, (from_point[0], from_point[1] + 1))
        members = self.add_to_basin(members, (from_point[0], from_point[1] - 1))
        return members

    def find_basin_size(self, start_point) -> int:
        basin_members = set()
        basin_members = self.grow_basin(basin_members, start_point)

        return len(basin_members)

    def find_basin_sizes(self) -> list:
        low_points, coords = self.find_low_points()
        basin_sizes = []
        for start_point in coords:
            basin_sizes.append(self.find_basin_size(start_point))

        return basin_sizes


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        height_data = []
        for line in dfile:
            height_data.append(line.strip())

        hm = Heightmap(height_data)
        basin_sizes = sorted(hm.find_basin_sizes(), reverse=True)

        print(f"Risk level: {hm.compute_risk_level()}")
        print(f"Three largest basin sizes: {basin_sizes[0:3]}")
        print(f"Product: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")
