class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy = nums[:]
        return nums + nums_copy
        