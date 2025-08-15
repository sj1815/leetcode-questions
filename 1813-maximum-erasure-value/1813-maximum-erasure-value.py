class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        seen = set()
        curr_sum = 0
        max_score = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left] 
                left += 1
            
            seen.add(nums[right])
            curr_sum += nums[right]
            max_score = max(max_score, curr_sum)
        
        return max_score

        