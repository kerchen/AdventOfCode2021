import pytest

from diagnostics import (find_most_common_bits, find_oxygen_rating,
                        to_binary_list, eliminate_readings, find_co2_rating)


test_data = [
    (["0100",
      "0100",
      "0101"], [0, 1, 0, 0]),
    (["1111",
      "0100",
      "0101"], [0, 1, 0, 1]),
    (["111111",
      "000000",
      "101010"], [1, 0, 1, 0, 1, 0]),
    (["00100",
      "11110",
      "10110",
      "10111",
      "10101",
      "01111",
      "00111",
      "11100",
      "10000",
      "11001",
      "00010",
      "01010"], [1, 0, 1, 1, 0])
]


@pytest.mark.parametrize("input_readings, expected_bits", test_data)
def test_most_correct_most_common_bits_returned(input_readings, expected_bits):
    computed_bits = find_most_common_bits(input_readings)

    assert computed_bits == expected_bits


binary_test_data = [
    ("0100", [0, 1, 0, 0]),
    ("1100", [1, 1, 0, 0]),
    ("0101", [0, 1, 0, 1]),
]


@pytest.mark.parametrize("input_value, expected_output", binary_test_data)
def test_binary_conversion(input_value, expected_output):
    computed_output = to_binary_list(input_value)

    assert computed_output == expected_output


eliminate_test_data = [
    (set(["0100", "1100", "1110"]), 0, 1, set(["1100", "1110"])),
    (set(["0100", "1100", "1110"]), 1, 1, set(["0100", "1100", "1110"])),
    (set(["0100", "1100", "1110"]), 2, 1, set(["1110"])),
    (set(["0100", "1100", "1110"]), 3, 1, set()),
    (set(["0100", "1100", "1110"]), 0, 0, set(["0100"])),
    (set(["0100", "1100", "1110"]), 1, 0, set()),
    (set(["0100", "1100", "1110"]), 2, 0, set(["0100", "1100"])),
    (set(["0100", "1100", "1110"]), 3, 0, set(["0100", "1100", "1110"])),
]


@pytest.mark.parametrize("input_set, bit_pos, keep_value, expected_output", eliminate_test_data)
def test_eliminate_readings(input_set, bit_pos, keep_value, expected_output):
    computed_set = eliminate_readings(input_set, bit_pos, keep_value)

    assert computed_set == expected_output


co2_test_data = [
    (["0101",
      "0000",
      "1111"], [1, 1, 1, 1]),
    (["01010",
      "11111"], [0, 1, 0, 1, 0]),
    (["00100",
      "11110",
      "10110",
      "10111",
      "10101",
      "01111",
      "00111",
      "11100",
      "10000",
      "11001",
      "00010",
      "01010"],
     [0, 1, 0, 1, 0])
]


@pytest.mark.parametrize("input_readings, expected_rating", co2_test_data)
def test_co2_rating(input_readings, expected_rating):
    computed_rating = find_co2_rating(input_readings)

    assert computed_rating == expected_rating


oxygen_test_data = [
    (["0100",
      "0100",
      "0101"], [0, 1, 0, 1]),
    (["0100",
      "0110",
      "0101"], [0, 1, 0, 1]),
    (["0100",
      "0111",
      "0101"], [0, 1, 0, 1]),
    (["0100",
      "0111",
      "1111",
      "0101"], [0, 1, 0, 1]),
    (["00100",
      "11110",
      "10110",
      "10111",
      "10101",
      "01111",
      "00111",
      "11100",
      "10000",
      "11001",
      "00010",
      "01010"], [1, 0, 1, 1, 1])
]


@pytest.mark.parametrize("input_readings, expected_rating", oxygen_test_data)
def test_oxygen_rating(input_readings, expected_rating):
    computed_rating = find_oxygen_rating(input_readings)

    assert computed_rating == expected_rating
