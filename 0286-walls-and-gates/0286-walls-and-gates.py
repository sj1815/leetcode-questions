class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        m, n = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        queue = deque()
        
        # Step 1: Enqueue all gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 2: BFS
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                # If it's a valid and empty room
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == INF:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))