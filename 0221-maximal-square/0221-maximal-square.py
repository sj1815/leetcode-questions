class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]
        max_length = 0

        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0 or matrix[i][j] == "0":
                return 0
            if memo[i][j] != -1: 
                return memo[i][j]
            
            memo[i][j] = 1 + min(
                dp(i - 1, j),
                dp(i, j - 1),
                dp(i - 1, j - 1)
            )
            return memo[i][j] 

        for i in range(rows):
            for j in range(cols):
                max_length = max(max_length, dp(i, j))

        return max_length * max_length

      

        