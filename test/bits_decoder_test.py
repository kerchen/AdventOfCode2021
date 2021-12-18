import pytest

from bits_decoder import (LiteralValuePacket, hex_to_binary, binary_to_int,
                          create_packet)


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
    assert isinstance(packet, LiteralValuePacket)
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


nested_mode0_test_data = [
    ('F40087D000BF10', 1, [8]),
    ('FC013BF0038F0AE422FF29558', 3, [5, 31, 1115])
]


@pytest.mark.parametrize("input_hex_sequence, expected_sub_count, expected_literal_values", nested_mode0_test_data)
def test_nested_mode0(input_hex_sequence, expected_sub_count, expected_literal_values):
    packet = create_packet(input_hex_sequence)

    assert len(packet.subpackets[0].subpackets) == expected_sub_count
    for i, ev in enumerate(expected_literal_values):
        assert packet.subpackets[0].subpackets[i].value == expected_literal_values[i]


operator_mode1_literals_test_data = [
    ('B6005CA10', [68]),
    ('B6015CA11CA11CA11CA11CA10', [68, 68, 68, 68, 68]),
]


@pytest.mark.parametrize("input_hex_sequence, expected_values", operator_mode1_literals_test_data)
def test_correct_literal_values_are_parsed_from_mode1_operator_packet(input_hex_sequence, expected_values):
    packet = create_packet(input_hex_sequence)
    literal_values = []
    for i, sp in enumerate(packet.subpackets):
        literal_values.append(sp.value)

    assert literal_values == expected_values

