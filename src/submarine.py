

def read_command_data(command_file: str) -> list:
    command_data = []

    with open(command_file, "r") as cfile:
        for line in cfile:
            command_data.append(line.strip())
    return command_data


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

    def command_boat(self, command_file: str):
        self.move(read_command_data(command_file))

        print(f"Final position: {self.position}")
        print(f"Final depth: {self.depth}")
        print(f"Product: {self.depth * self.position}")

