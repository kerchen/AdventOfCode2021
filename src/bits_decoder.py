from math import prod


SUM_PACKET_TYPE_ID = 0
PRODUCT_PACKET_TYPE_ID = 1
MINIMUM_PACKET_TYPE_ID = 2
MAXIMUM_PACKET_TYPE_ID = 3
LITERAL_VALUE_PACKET_TYPE_ID = 4
GREATER_THAN_PACKET_TYPE_ID = 5
LESS_THAN_PACKET_TYPE_ID = 6
EQUALS_PACKET_TYPE_ID = 7


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
        self.subpackets = []

    def sum_versions(self):
        version_sum = self.version
        for p in self.subpackets:
            version_sum += p.sum_versions()

        return version_sum

    def decode(self):
        return 0


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

    def decode(self):
        return self.value


class OperatorPacket(Packet):
    def __init__(self, version, bit_iterator: str, operation_fn: callable):
        super().__init__(version, bit_iterator)

        self.operation_fn = operation_fn
        mode_bit = next(bit_iterator)
        if mode_bit == '0':
            subpacket_bit_count = binary_to_int(extract_bit_sequence(bit_iterator, 15))
            subpacket_bit_iterator = iter(extract_bit_sequence(bit_iterator, subpacket_bit_count))
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

    def decode(self):
        subpacket_values = map(lambda p: p.decode(), self.subpackets)
        return self.operation_fn(subpacket_values)


def create_packet(hex_sequence: str) -> Packet:
    return create_packet_from_binary(iter(hex_to_binary(hex_sequence)))


def less_than(items: map) -> int:
    item_list = list(items)
    return 1 if item_list[0] < item_list[1] else 0


def greater_than(items: map) -> int:
    item_list = list(items)
    return 1 if item_list[0] > item_list[1] else 0


def equal(items: map) -> int:
    item_list = list(items)
    return 1 if item_list[0] == item_list[1] else 0


def create_packet_from_binary(bit_iterator: iter) -> Packet:
    operator_fns = {SUM_PACKET_TYPE_ID: sum,
                    PRODUCT_PACKET_TYPE_ID: prod,
                    MINIMUM_PACKET_TYPE_ID: min,
                    MAXIMUM_PACKET_TYPE_ID: max,
                    GREATER_THAN_PACKET_TYPE_ID: greater_than,
                    LESS_THAN_PACKET_TYPE_ID: less_than,
                    EQUALS_PACKET_TYPE_ID: equal}
    version = get_packet_version(bit_iterator)
    packet_type = get_packet_type(bit_iterator)

    if packet_type == LITERAL_VALUE_PACKET_TYPE_ID:
        return LiteralValuePacket(version, bit_iterator)
    else:
        return OperatorPacket(version, bit_iterator, operator_fns.get(packet_type, lambda *args: None))


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        hex_sequence = dfile.read()

        packet = create_packet(hex_sequence)
        print(f"Sum of versions: {packet.sum_versions()}")
        print(f"Decoded packet: {packet.decode()}")
