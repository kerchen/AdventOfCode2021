

class Riskmap:
    def __init__(self, input_risks: str):
        self.riskmap = dict()
        self.row_count = 0
        self.col_count = 0
        for r, row in enumerate(input_risks.split('\n')):
            self.col_count = len(row)
            for c, risk in enumerate(row):
                self.riskmap[(c, r)] = int(risk)

    def find_lowest_risk(self, c, r) -> int:
        return 9

    '''
    def find_lowest_neighbor(self, c, r, visited) -> tuple:
        risk = self.riskmap.get((c, r))
        if self.heightmap.get((c, r - 1), max_height) <= height:
            return False
        if self.heightmap.get((c, r + 1), max_height) <= height:
            return False
        if self.heightmap.get((c - 1, r), max_height) <= height:
            return False
        if self.heightmap.get((c + 1, r), max_height) <= height:
            return False

        return True
    '''