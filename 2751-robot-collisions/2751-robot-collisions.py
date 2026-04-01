class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []  # will store indices of robots moving right
        alive = [True] * len(positions)
        health = healths[:]  # copy
        
        for pos, h, d, i in robots:
            if d == 'R':
                stack.append(i)
            else:  # d == 'L'
                while stack and health[i] > 0:
                    j = stack[-1]  # last right-moving robot
                    
                    if health[j] < health[i]:
                        alive[j] = False
                        stack.pop()
                        health[i] -= 1
                    elif health[j] > health[i]:
                        alive[i] = False
                        health[j] -= 1
                        break
                    else:
                        alive[i] = False
                        alive[j] = False
                        stack.pop()
                        break
        
        # collect survivors in original order
        result = []
        for i in range(len(positions)):
            if alive[i]:
                result.append(health[i])
        
        return result
