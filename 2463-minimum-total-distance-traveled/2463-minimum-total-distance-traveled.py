class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        @lru_cache(None)
        def dfs(i, j):
            # all robots assigned
            if i == n:
                return 0
            
            # no factories left
            if j == m:
                return float('inf')
            
            res = dfs(i, j + 1)  # skip this factory
            
            pos, cap = factory[j]
            total = 0
            
            # try assigning k robots to this factory
            for k in range(cap):
                if i + k >= n:
                    break
                total += abs(robot[i + k] - pos)
                res = min(res, total + dfs(i + k + 1, j + 1))
            
            return res
        
        return dfs(0, 0)