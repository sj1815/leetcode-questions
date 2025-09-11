class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for balloon in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][balloon] + dp[balloon][right] + nums[left] * nums[balloon] * nums[right]
                    )

        return dp[0][n - 1]



        