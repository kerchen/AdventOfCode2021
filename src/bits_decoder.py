
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


def extract_bit_sequence(bit_iterator: iter, count: int) -> str:
    return ''.join([b for i in range(count) for b in next(bit_iterator)])


def get_packet_version(bit_iterator: iter) -> int:
    return binary_to_int(extract_bit_sequence(bit_iterator, 3))


def get_packet_type(bit_iterator: iter) -> int:
    return binary_to_int(extract_bit_sequence(bit_iterator, 3))


class Packet:
    def __init__(self, version: int, bit_iterator: str):
        self.version = version


class LiteralValuePacket(Packet):
    def __init__(self, version: int, bit_iterator: str):
        super().__init__(version, bit_iterator)

        payload = ''
        while True:
            bit = next(bit_iterator)
            payload = payload + extract_bit_sequence(bit_iterator, 4)
            if bit == '0':
                break

        self.value = binary_to_int(payload)


class OperatorPacket(Packet):
    def __init__(self, version, bit_iterator: str):
        super().__init__(version, bit_iterator)

        self.subpacket_bit_count = 0
        self.subpackets = []
        mode_bit = next(bit_iterator)
        if mode_bit == '0':
            self.subpacket_bit_count = binary_to_int(extract_bit_sequence(bit_iterator, 15))
            subpacket_bit_iterator = iter(extract_bit_sequence(bit_iterator, self.subpacket_bit_count))
            while True:
                try:
                    packet = create_packet_from_binary(subpacket_bit_iterator)
                    self.subpackets.append(packet)
                except StopIteration:
                    break
        else:
            subpacket_count = binary_to_int(extract_bit_sequence(bit_iterator, 11))
            while subpacket_count:
                packet = create_packet_from_binary(bit_iterator)
                self.subpackets.append(packet)
                subpacket_count -= 1


def create_packet(hex_sequence: str) -> Packet:
    return create_packet_from_binary(iter(hex_to_binary(hex_sequence)))


def create_packet_from_binary(bit_iterator: iter) -> Packet:
    version = get_packet_version(bit_iterator)
    packet_type = get_packet_type(bit_iterator)

    if packet_type == LITERAL_VALUE_PACKET_TYPE_ID:
        return LiteralValuePacket(version, bit_iterator)
    else:
        return OperatorPacket(version, bit_iterator)
