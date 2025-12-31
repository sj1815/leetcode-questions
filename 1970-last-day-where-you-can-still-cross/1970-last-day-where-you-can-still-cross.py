class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            queue = collections.deque()

            # Mark flooded cells
            for r, c in cells[:day]:
                grid[r - 1][c - 1] = 1

            # Start BFS from top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = -1  # visited

            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        queue.append((nr, nc))

            return False

        # Binary search on days
        left, right = 1, row * col
        while left < right:
            mid = right - (right - left) // 2
            if canCross(mid):
                left = mid
            else:
                right = mid - 1

        return left