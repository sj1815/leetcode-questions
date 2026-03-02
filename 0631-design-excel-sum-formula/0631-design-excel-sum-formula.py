from typing import List
from collections import defaultdict

class Excel:

    def __init__(self, height: int, width: str):
        self.values = defaultdict(int)      # actual cell values
        self.formulas = {}                  # cell -> {ref_cell: count}
        self.dependents = defaultdict(set)  # reverse graph

    def _key(self, row, column):
        return (row, column)

    def _parse(self, s):
        col = s[0]
        row = int(s[1:])
        return (row, col)

    def _get_cells_from_range(self, s):
        if ':' not in s:
            yield self._parse(s)
        else:
            start, end = s.split(':')
            r1, c1 = self._parse(start)
            r2, c2 = self._parse(end)

            for r in range(r1, r2 + 1):
                for c in range(ord(c1), ord(c2) + 1):
                    yield (r, chr(c))

    def _update_dependents(self, cell, delta):
        for dep in self.dependents[cell]:
            self.values[dep] += delta * self.formulas[dep][cell]
            self._update_dependents(dep, delta * self.formulas[dep][cell])

    def set(self, row: int, column: str, val: int) -> None:
        cell = (row, column)

        # Remove old formula
        if cell in self.formulas:
            for ref in self.formulas[cell]:
                self.dependents[ref].remove(cell)
            del self.formulas[cell]

        delta = val - self.values[cell]
        self.values[cell] = val

        self._update_dependents(cell, delta)

    def get(self, row: int, column: str) -> int:
        return self.values[(row, column)]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = (row, column)

        # Remove old formula if exists
        if cell in self.formulas:
            for ref in self.formulas[cell]:
                self.dependents[ref].remove(cell)

        counter = defaultdict(int)
        total = 0

        for s in numbers:
            for ref in self._get_cells_from_range(s):
                counter[ref] += 1
                total += self.values[ref]

        self.formulas[cell] = counter

        for ref in counter:
            self.dependents[ref].add(cell)

        delta = total - self.values[cell]
        self.values[cell] = total

        self._update_dependents(cell, delta)

        return total

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)