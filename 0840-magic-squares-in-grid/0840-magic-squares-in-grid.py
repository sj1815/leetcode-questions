class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def isMagic(r, c):
            if grid[r+1][c+1] != 5:
                return False
            
            seen = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)
            
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != 15:
                    return False
                if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != 15:
                    return False
            
            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False
            
            return True
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1
        
        return count