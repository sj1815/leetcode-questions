class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            next_dp = dp[:]   
            
            for r in range(3):
                if dp[r] == float('-inf'):
                    continue
                
                new_sum = dp[r] + num
                next_dp[new_sum % 3] = max(next_dp[new_sum % 3], new_sum)
            
            dp = next_dp
        
        return dp[0]