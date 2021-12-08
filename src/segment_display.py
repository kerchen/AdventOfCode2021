

def parse_input_line(input_line: str) -> tuple:
    signal_pattern_str, display_value_str = input_line.split(' | ')
    return signal_pattern_str.split(' '), display_value_str.split(' ')


def solve_p1(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        signal_patterns = []
        display_values = []
        for line in dfile:
            pattern, value = parse_input_line(line.strip())
            signal_patterns.append(pattern)
            display_values.append(value)

        unique_pattern_lengths = [2, 3, 4, 7]
        count = 0
        for value_list in display_values:
            for v in value_list:
                if len(v) in unique_pattern_lengths:
                    count += 1
        print(f"Number of display values with unique pattern lengths: {count}")