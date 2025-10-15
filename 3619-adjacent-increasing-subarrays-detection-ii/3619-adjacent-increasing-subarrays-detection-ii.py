class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1

        prev = 0
        curr = 1
        max_k = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                max_k = max(max_k, max(curr//2, min(curr, prev)))
                prev = curr
                curr = 1
        max_k = max(max_k, max(curr//2, min(curr, prev)))
        return max_k
        