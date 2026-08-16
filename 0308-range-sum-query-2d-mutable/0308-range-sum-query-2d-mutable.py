class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m else 0

        self.matrix = [row[:] for row in matrix]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for r in range(self.m):
            for c in range(self.n):
                self._add(r, c, matrix[r][c])

    def _add(self, row: int, col: int, delta: int) -> None:
        r = row + 1

        while r <= self.m:
            c = col + 1

            while c <= self.n:
                self.bit[r][c] += delta
                c += c & -c

            r += r & -r

    def _sum(self, row: int, col: int) -> int:
        """Sum of rectangle (0,0) to (row,col)."""
        if row < 0 or col < 0:
            return 0

        res = 0
        r = row + 1

        while r > 0:
            c = col + 1

            while c > 0:
                res += self.bit[r][c]
                c -= c & -c

            r -= r & -r

        return res

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        self._add(row, col, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._sum(row2, col2)
            - self._sum(row1 - 1, col2)
            - self._sum(row2, col1 - 1)
            + self._sum(row1 - 1, col1 - 1)
        )