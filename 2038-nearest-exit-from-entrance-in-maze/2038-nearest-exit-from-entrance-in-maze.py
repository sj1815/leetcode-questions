class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = collections.deque()
        queue.append((entrance[0], entrance[1], 0))  # row, col, steps
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        maze[entrance[0]][entrance[1]] = "+" #mark entrance as visited

        while queue:
            row, col, steps = queue.popleft()
            for dr, dc in dirs:
                r = row + dr
                c =  col + dc
                if 0 <= r < rows and 0 <= c < cols and maze[r][c] == ".":
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        return steps + 1
                    
                    maze[r][c] = "+"
                    queue.append((r, c, steps + 1))

        return -1


