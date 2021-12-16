from math import ceil

PACKET_VERSION_START_BIT = 0
PACKET_VERSION_END_BIT = 2
PACKET_TYPE_START_BIT = 3
PACKET_TYPE_END_BIT = 5

LITERAL_VALUE_PACKET_TYPE_ID = 4


class Error(BaseException):
    pass


class NotImplementedYetError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


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


def get_packet_version(hex_sequence: str) -> int:
    binary_sequence = hex_to_binary(hex_sequence)

    return binary_to_int(binary_sequence[PACKET_VERSION_START_BIT:PACKET_VERSION_END_BIT+1])


def get_packet_type(hex_sequence: str) -> int:
    binary_sequence = hex_to_binary(hex_sequence)

    return binary_to_int(binary_sequence[PACKET_TYPE_START_BIT:PACKET_TYPE_END_BIT+1])


class Packet:
    def __init__(self, hex_sequence: str):
        self.version = get_packet_version(hex_sequence)
        self.type = get_packet_type(hex_sequence)
        self.bytes_consumed = 0


class LiteralValuePacket(Packet):
    def __init__(self, hex_sequence: str):
        super().__init__(hex_sequence)

        binary_sequence = hex_to_binary(hex_sequence)
        payload = ''
        bi = PACKET_TYPE_END_BIT + 1
        while bi < len(binary_sequence):
            if binary_sequence[bi] == '1':
                payload = payload + binary_sequence[bi+1:bi+5]
                bi += 5
            else:
                payload = payload + binary_sequence[bi+1:bi+5]
                bi += 5
                break

        self.bytes_consumed = ceil(bi/8)
        self.value = binary_to_int(payload)


def create_packet(hex_sequence: str) -> Packet:
    packet_type = get_packet_type(hex_sequence)

    if packet_type == LITERAL_VALUE_PACKET_TYPE_ID:
        return LiteralValuePacket(hex_sequence)

    raise NotImplementedError("Unknown packet type")
