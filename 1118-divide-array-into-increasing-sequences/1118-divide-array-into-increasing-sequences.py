class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if n < k:
            return False

        freq = Counter(nums)
        max_freq = max(freq.values())

        return max_freq * k <= n        