class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0  
        
        x = y = 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1: 
                d = (d + 1) % 4
            elif cmd == -2: 
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist