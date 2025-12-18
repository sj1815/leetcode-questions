class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0

        for num in nums:
            if n < 2 or num != nums[n - 2]:
                nums[n] = num
                n += 1
        
        return n