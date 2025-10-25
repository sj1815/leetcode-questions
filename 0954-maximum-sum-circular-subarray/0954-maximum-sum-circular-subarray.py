class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        curr_max, max_sum = 0, nums[0]
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
        
        curr_min, min_sum = 0, nums[0]
        for num in nums:
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        if total_sum == min_sum:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)