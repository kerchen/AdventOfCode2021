import pytest

from bits_decoder import (hex_to_binary, binary_to_int, get_packet_version,
                          get_packet_type, create_packet)


hex_to_binary_conversion_test_data = [
    ('0', '0000'),
    ('1', '0001'),
    ('7', '0111'),
    ('8', '1000'),
    ('A', '1010'),
    ('F', '1111'),
    ('01BCF', '00000001101111001111'),
]


@pytest.mark.parametrize("input_hex_sequence, expected_binary_sequence", hex_to_binary_conversion_test_data)
def test_hex_to_binary_produces_correct_sequences(input_hex_sequence, expected_binary_sequence):
    binary_sequence = hex_to_binary(input_hex_sequence)
    assert binary_sequence == expected_binary_sequence


binary_to_int_conversion_test_data = [
    ('0', 0),
    ('10101', 21),
    ('111', 7),
    ('1000', 8),
    ('1010', 10),
    ('11111', 31),
    ('101000101011010', 20826)
]


@pytest.mark.parametrize("input_binary_sequence, expected_value", binary_to_int_conversion_test_data)
def test_binary_to_int_conversion_works_correctly(input_binary_sequence, expected_value):
    value = binary_to_int(input_binary_sequence)
    assert value == expected_value


packet_header_version_parsing_test_data = [
    ('00', 0),
    ('FF', 7),
    ('21', 1),
    ('CD', 6),
]


@pytest.mark.parametrize("input_hex_sequence, expected_version", packet_header_version_parsing_test_data)
def test_correct_packet_version_found(input_hex_sequence, expected_version):
    packet_version = get_packet_version(input_hex_sequence)
    assert packet_version == expected_version


packet_header_type_parsing_test_data = [
    ('00', 0),
    ('FF', 7),
    ('21', 0),
    ('CD', 3),
]


@pytest.mark.parametrize("input_hex_sequence, expected_type", packet_header_type_parsing_test_data)
def test_correct_packet_type_found(input_hex_sequence, expected_type):
    packet_type = get_packet_type(input_hex_sequence)
    assert packet_type == expected_type


literal_value_test_data = [
    ('3000', 0),
    ('F210800', 0),
    ('F00', 0),
    ('F210830', 12),
    ('121A924', 2601),
    ('D2FE28', 2021)
]


@pytest.mark.parametrize("input_hex_sequence, expected_value", literal_value_test_data)
def test_correct_literal_value_is_computed(input_hex_sequence, expected_value):
    packet = create_packet(input_hex_sequence)
    assert packet.type == 4
    literal_value = packet.value
    assert literal_value == expected_value


operator_mode0_test_data = [
    ('E40000', 0),
    ('F4002FC30', 11),  # 1 literal value 6
    ('F4006FC379918', 27),  # 2 literal values 6, 147
    ('38006F45291200', 27),  # 2 literal values 10, 21
    ('F400C3C37991F93B00', 48)  # 3 literal values 6, 147, 864
]


@pytest.mark.parametrize("input_hex_sequence, expected_value", operator_mode0_test_data)
def test_correct_bit_length_is_found_for_mode0_operator(input_hex_sequence, expected_value):
    packet = create_packet(input_hex_sequence)

    assert packet.subpacket_bit_count == expected_value


operator_mode0_literals_test_data = [
    ('F4002FC30', [6]),
    ('F4006FC379918', [6, 147]),
    ('38006F45291200', [10, 20]),
    ('F400C3C37991F93B00', [6, 147, 864])
]


@pytest.mark.parametrize("input_hex_sequence, expected_values", operator_mode0_literals_test_data)
def test_correct_literal_values_are_parsed_from_mode0_operator_packet(input_hex_sequence, expected_values):
    packet = create_packet(input_hex_sequence)
    literal_values = []
    for i, sp in enumerate(packet.subpackets):
        literal_values.append(sp.value)

    assert literal_values == expected_values


def test_nested_mode0():
    packet = create_packet('F40087D000BF10')

    assert len(packet.subpackets) == 1
    assert packet.subpackets[0].subpackets[0].value == 8
