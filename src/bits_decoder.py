
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

    return binary_to_int(binary_sequence[0:3])


def get_packet_type(hex_sequence: str) -> int:
    binary_sequence = hex_to_binary(hex_sequence)

    return binary_to_int(binary_sequence[3:6])
