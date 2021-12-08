

def parse_input_line(input_line: str) -> tuple:
    signal_pattern_str, display_value_str = input_line.split(' | ')
    return signal_pattern_str.split(' '), display_value_str.split(' ')
