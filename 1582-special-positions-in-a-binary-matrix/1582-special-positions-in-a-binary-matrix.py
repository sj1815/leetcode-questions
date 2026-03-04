class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        
        res = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1 and row_count[row] == 1 and col_count[col] == 1:
                    res += 1

        return res