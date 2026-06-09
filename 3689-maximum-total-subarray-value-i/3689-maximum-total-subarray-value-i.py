class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1, m2 = min(nums), max(nums)
        return (m2 - m1) * k