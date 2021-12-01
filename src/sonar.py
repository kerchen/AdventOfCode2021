import argparse


class DepthStatistics:
    def __init__(self, window_size=1):
        self.window_size = window_size
        self.reading_count = 0
        self.increase_count = 0


def get_depth_stats(depth_data: list, window_size: int = 1) -> DepthStatistics:
    stats = DepthStatistics(window_size)

    stats.reading_count = len(depth_data)
    if stats.reading_count >= window_size:
        window = []
        for i in range(window_size):
            window.append(depth_data[i])
        previous_sum = sum(window)
        for depth in depth_data[window_size:]:
            window.pop(0)
            window.append(depth)
            current_sum = sum(window)
            if previous_sum < current_sum:
                stats.increase_count += 1
            previous_sum = current_sum

    return stats


def read_depth_data(depth_file: str) -> list:
    depth_data = []

    with open(depth_file, "r") as dfile:
        for line in dfile:
            depth_data.append(int(line.strip()))
    return depth_data


def print_depth_stats(depth_file: str, depth_stats: DepthStatistics):
    print(f"Stats for {depth_file}:")
    print(f"Number of readings: {depth_stats.reading_count}")
    print(f"Sliding window size: {depth_stats.window_size}")
    print(f"Number of increases: {depth_stats.increase_count}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--depth-file', help='Text file containing depth readings')
    parser.add_argument('--window-size', type='int', default=1, help='Size of the sliding window')
    args = parser.parse_args()

    if args.depth_file:
        depth_data = read_depth_data(args.depth_file)
        depth_stats = get_depth_stats(depth_data, args.window_size)
        print_depth_stats(args.depth_file, depth_stats)
