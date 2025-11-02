class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        # 0 = Free, 1 = Gaurd, 2 = Wall, 3 = Gaurdable

        for r, c in guards:
            grid[r][c] = 1
        
        for r, c in walls:
            grid[r][c] = 2

        def markGaurded(r, c):
            # Down
            for row in range(r + 1, m):
                if grid[row][c] in (1, 2):
                    break
                grid[row][c] = 3
            
            # Up
            for row in range(r - 1, -1, -1):
                if grid[row][c] in (1, 2):
                    break
                grid[row][c] = 3

            # Right
            for col in range(c + 1, n):
                if grid[r][col] in (1, 2):
                    break
                grid[r][col] = 3

            # Left
            for col in range(c - 1, -1, -1):
                if grid[r][col] in (1, 2):
                    break
                grid[r][col] = 3

        for r, c in guards:
            markGaurded(r, c)

        res = 0
        for row in grid:
            for n in row:
                if n == 0:
                    res += 1

        return res


