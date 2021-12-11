
class Octogrid:
    def __init__(self, energy_levels: list):
        self.energy = dict()
        self.row_count = len(energy_levels)
        self.col_count = 0
        for r, row in enumerate(energy_levels):
            self.col_count = len(row)
            for c, e in enumerate(row):
                self.energy[(c, r)] = int(e)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Octogrid):
            return NotImplemented

        return self.energy == other.energy

    def flash_neighbors(self, c: int, r: int):
        for cc in range(c-1, c+2):
            for rr in range(r-1, r+2):
                if rr < 0 or cc < 0 or rr >= self.row_count or cc >= self.col_count:
                    continue
                if rr == r and cc == c:
                    continue
                old_e = self.energy[(cc, rr)]
                new_e = old_e + 1
                self.energy[(cc, rr)] = new_e
                if (old_e <= 9) and (new_e > 9):
                    self.flash_neighbors(cc, rr)

    def step_time(self, steps: int) -> int:
        flash_count = 0
        for s in range(steps):
            for r in range(self.row_count):
                for c in range(self.col_count):
                    old_e = self.energy[(c, r)]
                    new_e = old_e + 1
                    self.energy[(c, r)] = new_e
                    if (old_e <= 9) and (new_e > 9):
                        self.flash_neighbors(c, r)

            for r in range(self.row_count):
                for c in range(self.col_count):
                    if self.energy[(c, r)] > 9:
                        flash_count += 1
                        self.energy[(c, r)] = 0;

        return flash_count


def solve(input_data_file: str):
    with open(input_data_file, "r") as dfile:
        starting_energy = []
        for line in dfile:
            starting_energy.append(line.strip())

        g = Octogrid(starting_energy)
        print(f"Flashes after 100 steps: {g.step_time(100)}")

        g2 = Octogrid(starting_energy)
        t = 0
        while(True):
            t += 1
            if 100 == g2.step_time(1):
                print(f"First simultaneous flash at time {t}")
                break
