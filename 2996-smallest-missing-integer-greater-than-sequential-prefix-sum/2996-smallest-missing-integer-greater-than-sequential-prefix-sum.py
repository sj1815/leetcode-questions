class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        for a, b in pairwise(nums):
            if b == a + 1:
                total += b
            else:
                break

        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total