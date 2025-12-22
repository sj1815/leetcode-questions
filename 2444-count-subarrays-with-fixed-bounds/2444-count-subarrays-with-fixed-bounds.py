class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_position = max_position = left_bound = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = i
            
            if num == minK:
                min_position = i
            if num == maxK:
                max_position = i

            count += max(0, min(min_position, max_position) - left_bound)
        
        return count