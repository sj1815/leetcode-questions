class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        rows = Counter(tuple(row) for row in grid)

        for c in range(n):
            cols = tuple(grid[r][c] for r in range(n))
            count += rows[cols]
        
        return count

