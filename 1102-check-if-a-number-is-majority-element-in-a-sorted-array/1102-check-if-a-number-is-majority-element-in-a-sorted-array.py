class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counts = Counter(nums)
        return counts[target] > len(nums) // 2
        