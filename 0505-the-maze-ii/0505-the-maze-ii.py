class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        INF = float('inf')
        
        dist = [[INF] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        
        pq = [(0, start[0], start[1])]  # (distance, r, c)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            d, r, c = heapq.heappop(pq)

            if [r, c] == destination:
                return d

            if d > dist[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r, c
                steps = 0

                # roll until wall
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1

                if dist[r][c] + steps < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + steps
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))

        return -1
