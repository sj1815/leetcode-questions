class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache(None)

        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i == 2:
                return 2
            
            return (2 * dp(i - 1) + dp(i - 3)) % ((10**9) + 7)

        return dp(n)