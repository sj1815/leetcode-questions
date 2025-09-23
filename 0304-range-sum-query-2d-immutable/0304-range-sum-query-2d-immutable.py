class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])

        # prefix_sum[r][c] = sum of all elements in rectangle (0,0) → (r-1, c-1)
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.prefix_sum[r][c] = (
                    self.prefix_sum[r][c - 1]   # sum of rectangle to the LEFT
                    + self.prefix_sum[r - 1][c] # sum of rectangle ABOVE
                    - self.prefix_sum[r - 1][c - 1] # subtract overlap
                    + matrix[r - 1][c - 1]     # add current element
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # convert to 1-based indexing (prefix_sum has extra row+col padding)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # inclusion-exclusion principle
        return (
            self.prefix_sum[row2][col2]        # total up to (row2, col2)
            - self.prefix_sum[row1 - 1][col2]  # remove rows above row1
            - self.prefix_sum[row2][col1 - 1]  # remove cols left of col1
            + self.prefix_sum[row1 - 1][col1 - 1]  # add back overlap
        )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)