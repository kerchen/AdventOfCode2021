from math import pow


def read_readings(readings_file: str) -> list:
    readings = []

    with open(readings_file, "r") as rfile:
        for line in rfile:
            readings.append(line.strip())
    return readings


def binary_to_base10(bits: list) -> int:
    result = 0
    bit_count = len(bits)
    for i in range(bit_count):
        if bits[i]:
            result += pow(2, bit_count - i - 1)
    return result


def find_most_common_bits(input_readings: list, bias: int = 0) -> list:
    bit_count = len(input_readings[0])
    counts = [0] * bit_count
    for reading in input_readings:
        for i in range(bit_count):
            if reading[i] == '1':
                counts[i] += 1

    result = [0] * bit_count
    for i in range(bit_count):
        if bias:
            if counts[i] >= len(input_readings) / 2:
                result[i] = 1
        else:
            if counts[i] > len(input_readings) / 2:
                result[i] = 1

    return result


def to_binary_list(value: str) -> list:
    result = []
    for d in value:
        result.append(0 if d == '0' else 1)

    return result


def eliminate_readings(readings: set, bit_pos: int, keep_value: int) -> set:
    reduced_readings = set()
    for r in readings:
        if int(r[bit_pos]) == keep_value:
            reduced_readings.add(r)

    return reduced_readings


def find_oxygen_rating(input_readings: list) -> list:
    common_bits = find_most_common_bits(input_readings, bias=1)
    bit_count = len(common_bits)

    remaining_readings = set(input_readings)
    bit_pos = 0
    while len(remaining_readings) > 1 and bit_pos < bit_count:
        remaining_readings = eliminate_readings(remaining_readings, bit_pos, common_bits[bit_pos])
        common_bits = find_most_common_bits(list(remaining_readings), bias=1)
        bit_pos += 1

    return to_binary_list(remaining_readings.pop())


def invert(bits: list) -> list:
    return_list = []
    for b in bits:
        if b == 0:
            return_list.append(1)
        else:
            return_list.append(0)

    return return_list


def find_co2_rating(input_readings: list) -> list:
    common_bits = invert(find_most_common_bits(input_readings, bias=1))
    bit_count = len(common_bits)

    remaining_readings = set(input_readings)
    bit_pos = 0
    while len(remaining_readings) > 1 and bit_pos < bit_count:
        remaining_readings = eliminate_readings(remaining_readings, bit_pos, common_bits[bit_pos])
        common_bits = invert(find_most_common_bits(list(remaining_readings), bias=1))
        bit_pos += 1

    return to_binary_list(remaining_readings.pop())


def compute_rates(bits: list) -> tuple:
    gamma = 0
    epsilon = 0
    bit_count = len(bits)
    for i in range(bit_count):
        if bits[i]:
            gamma += pow(2, bit_count-i-1)
        else:
            epsilon += pow(2, bit_count-i-1)

    print(f"Gamma: {gamma}")
    print(f"Epsilon: {epsilon}")
    print(f"Product: {gamma*epsilon}")

    return gamma, epsilon