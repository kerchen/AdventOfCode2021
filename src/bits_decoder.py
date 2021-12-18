
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
    def __init__(self, version: int, binary_sequence: str):
        self.version = version
        self.bits_consumed = 6


class LiteralValuePacket(Packet):
    def __init__(self, version: int, binary_sequence: str):
        super().__init__(version, binary_sequence)

        payload = ''
        bi = self.bits_consumed
        while bi < len(binary_sequence):
            if binary_sequence[bi] == '1':
                payload = payload + binary_sequence[bi+1:bi+5]
                bi += 5
            else:
                payload = payload + binary_sequence[bi+1:bi+5]
                bi += 5
                break

        self.bits_consumed = bi
        self.value = binary_to_int(payload)


def mode0_data_size(binary_sequence: str) -> tuple:
    mode0_bit_count = 15
    mode0_start_data_bit = 0
    mode0_end_data_bit = mode0_start_data_bit + mode0_bit_count
    return binary_to_int(binary_sequence[mode0_start_data_bit:mode0_end_data_bit]), mode0_end_data_bit + 1


class OperatorPacket(Packet):
    def __init__(self, version, binary_sequence: str):
        super().__init__(version, binary_sequence)
        mode_bit = PACKET_HEADER_END_BIT + 1

        self.subpacket_bit_count = 0
        self.subpackets = []
        if binary_sequence[mode_bit] == '0':
            self.subpacket_bit_count, next_bit = mode0_data_size(binary_sequence[mode_bit+1:])
            self.bits_consumed += self.subpacket_bit_count + next_bit
            bits_remaining = self.subpacket_bit_count
            while bits_remaining:
                packet = create_packet_from_binary(binary_sequence[mode_bit+next_bit:])
                bits_remaining -= packet.bits_consumed
                next_bit += packet.bits_consumed
                self.subpackets.append(packet)


def create_packet(hex_sequence: str) -> Packet:
    return create_packet_from_binary(hex_to_binary(hex_sequence))


def create_packet_from_binary(binary_sequence: str) -> Packet:
    bit_iterator = iter(binary_sequence)
    version = get_packet_version(bit_iterator)
    packet_type = get_packet_type(bit_iterator)

    if packet_type == LITERAL_VALUE_PACKET_TYPE_ID:
        return LiteralValuePacket(version, binary_sequence)
    else:
        return OperatorPacket(version, binary_sequence)
