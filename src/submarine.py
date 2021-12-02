
class Submarine:
    def __init__(self):
        self.position = 0
        self.depth = 0

    def move(self, commands: list):
        for full_command in commands:
            command, amount = full_command.split()
            if command == 'forward':
                self.position += int(amount)
            elif command == 'down':
                self.depth += int(amount)
            elif command == 'up':
                self.depth -= int(amount)


def read_command_data(command_file: str) -> list:
    command_data = []

    with open(command_file, "r") as cfile:
        for line in cfile:
            command_data.append(line.strip())
    return command_data


def command_sub(command_file: str):
    command_data = read_command_data(command_file)
    boat = Submarine()

    boat.move(command_data)

    print(f"Final position: {boat.position}")
    print(f"Final depth: {boat.depth}")
    print(f"Product: {boat.depth * boat.position}")

