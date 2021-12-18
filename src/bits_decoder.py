
PACKET_HEADER_END_BIT = 5
LITERAL_VALUE_PACKET_TYPE_ID = 4


def hex_to_binary(hex_str: str) -> str:
    hex_binary_map = {'0': '0000',
                      '1': '0001',
                      '2': '0010',
                      '3': '0011',
                      '4': '0100',
                      '5': '0101',
                      '6': '0110',
                      '7': '0111',
                      '8': '1000',
                      '9': '1001',
                      'A': '1010',
                      'B': '1011',
                      'C': '1100',
                      'D': '1101',
                      'E': '1110',
                      'F': '1111'}
    binary_sequence = ''
    for h in hex_str:
        binary_sequence = binary_sequence + hex_binary_map[h]

    return binary_sequence


def binary_to_int(binary_sequence: str) -> int:
    return_value = 0
    for bd in binary_sequence:
        return_value *= 2
        return_value += (1 if bd == '1' else 0)
    return return_value


def get_packet_version(bit_iterator: iter) -> int:
    binary_sequence = ''.join([b for i in range(3) for b in next(bit_iterator)])
    return binary_to_int(binary_sequence)


def get_packet_type(bit_iterator: iter) -> int:
    binary_sequence = ''.join([b for i in range(3) for b in next(bit_iterator)])
    return binary_to_int(binary_sequence)


class Packet:
    def __init__(self, version: int, bit_iterator: str):
        self.version = version


class LiteralValuePacket(Packet):
    def __init__(self, version: int, bit_iterator: str):
        super().__init__(version, bit_iterator)

        payload = ''
        read_another = True
        while read_another:
            bit = next(bit_iterator)
            bit_sequence = ''.join([b for i in range(4) for b in next(bit_iterator)])
            payload = payload + bit_sequence
            if bit == '0':
                read_another = False

        self.value = binary_to_int(payload)


def mode0_data_size(bit_iterator: iter) -> int:
    bit_sequence = ''.join([b for i in range(15) for b in next(bit_iterator)])

    return binary_to_int(bit_sequence)


class OperatorPacket(Packet):
    def __init__(self, version, bit_iterator: str):
        super().__init__(version, bit_iterator)

        self.subpacket_bit_count = 0
        self.subpackets = []
        mode_bit = next(bit_iterator)
        if mode_bit == '0':
            self.subpacket_bit_count = mode0_data_size(bit_iterator)
            subpacket_bit_iterator = iter(''.join([b for i in range(self.subpacket_bit_count) for b in next(bit_iterator)]))
            while True:
                try:
                    packet = create_packet_from_binary(subpacket_bit_iterator)
                    self.subpackets.append(packet)
                except StopIteration:
                    break


def create_packet(hex_sequence: str) -> Packet:
    return create_packet_from_binary(iter(hex_to_binary(hex_sequence)))


def create_packet_from_binary(bit_iterator: iter) -> Packet:
    version = get_packet_version(bit_iterator)
    packet_type = get_packet_type(bit_iterator)

    if packet_type == LITERAL_VALUE_PACKET_TYPE_ID:
        return LiteralValuePacket(version, bit_iterator)
    else:
        return OperatorPacket(version, bit_iterator)
