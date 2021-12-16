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
    ('38006F45291200', 27)
]


@pytest.mark.parametrize("input_hex_sequence, expected_value", operator_mode0_test_data)
def test_correct_bit_length_is_found_for_mode0_operator(input_hex_sequence, expected_value):
    packet = create_packet(input_hex_sequence)

    assert packet.subpacket_bit_count == expected_value
