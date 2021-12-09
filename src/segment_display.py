

def parse_input_line(input_line: str) -> tuple:
    signal_pattern_str, display_value_str = input_line.split(' | ')
    return signal_pattern_str.split(' '), display_value_str.split(' ')


def get_set_for_length(signal_patterns: list, length: int) -> set:
    for pattern in signal_patterns:
        if len(pattern) == length:
            return set(pattern)

    return None


def deduce_a(signal_patterns: list) -> set:
    cf_set = get_set_for_length(signal_patterns, 2)
    acf_set = get_set_for_length(signal_patterns, 3)

    return acf_set - cf_set


def deduce_bd(signal_patterns: list) -> set:
    cf_set = get_set_for_length(signal_patterns, 2)
    bcdf_set = get_set_for_length(signal_patterns, 4)

    return bcdf_set - cf_set


def deduce_eg(signal_patterns: list) -> set:
    acf_set = get_set_for_length(signal_patterns, 3)
    bcdf_set = get_set_for_length(signal_patterns, 4)
    all_set = get_set_for_length(signal_patterns, 7)

    return all_set - bcdf_set - acf_set


def deduce_digits(signal_patterns: list, display_values: list) -> int:
    eg_set = deduce_eg(signal_patterns)
    bd_set = deduce_bd(signal_patterns)
    acf_set = get_set_for_length(signal_patterns, 3)

    return_digits = 0
    for dv in display_values:
        if len(dv) == 2:
            return_digits = return_digits * 10 + 1
        elif len(dv) == 3:
            return_digits = return_digits * 10 + 7
        elif len(dv) == 4:
            return_digits = return_digits * 10 + 4
        elif len(dv) == 7:
            return_digits = return_digits * 10 + 8
        elif len(dv) == 5:
            if eg_set.intersection(set(dv)) == eg_set:
                return_digits = return_digits * 10 + 2
            elif bd_set.intersection(set(dv)) == bd_set:
                return_digits = return_digits * 10 + 5
            else:
                return_digits = return_digits * 10 + 3
        else:
            if not bd_set.intersection(set(dv)) == bd_set:
                return_digits = return_digits * 10 + 0
            elif acf_set.intersection(set(dv)) == acf_set:
                return_digits = return_digits * 10 + 9
            else:
                return_digits = return_digits * 10 + 6

    return return_digits


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        signal_patterns = []
        display_values = []
        digits_sum = 0
        for line in dfile:
            pattern, value = parse_input_line(line.strip())
            signal_patterns.append(pattern)
            display_values.append(value)
            digits_sum += deduce_digits(pattern, value)

        unique_patterns = {2: 'cf', 3: 'acf', 4: 'bcdf', 7: 'abcdefg'}
        count = 0
        for value_list in display_values:
            for v in value_list:
                pattern_length = len(v)
                if pattern_length in unique_patterns:
                    count += 1

        print(f"Number of display values with unique pattern lengths: {count}")
        print(f"Sum of digits: {digits_sum}")