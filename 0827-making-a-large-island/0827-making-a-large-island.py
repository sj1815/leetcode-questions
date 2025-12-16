class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # start from 2 to avoid confusion with 0 and 1
        area_map = {}

        def dfs(r, c, island_id):
            stack = [(r, c)]
            area = 0
            grid[r][c] = island_id

            while stack:
                x, y = stack.pop()
                area += 1

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island_id
                        stack.append((nx, ny))

            return area


        # Label islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area_map[island_id] = dfs(i, j, island_id)
                    island_id += 1

        res = max(area_map.values(), default=0)

        # Try flipping each 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    area = 1  # flip this 0

                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            idx = grid[ni][nj]
                            if idx > 1 and idx not in seen:
                                seen.add(idx)
                                area += area_map[idx]

                    res = max(res, area)

        return res

    