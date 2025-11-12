class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
    
        if ones > 0:
            return n - ones
        
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i)
                    break 
        
        if min_len == float('inf'):
            return -1
        
        return min_len + n - 1
