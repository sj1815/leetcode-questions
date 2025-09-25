class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @lru_cache(None)
        def dfs(r, c):
            if r == n - 1:
                return triangle[r][c]
            
            return triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
        
        return dfs(0, 0)