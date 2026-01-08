class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        queue = deque([tuple(start)])
        visited.add(tuple(start))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True

            for dr, dc in directions:
                nr, nc = r, c

                # Roll until hitting a wall
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc

                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return False