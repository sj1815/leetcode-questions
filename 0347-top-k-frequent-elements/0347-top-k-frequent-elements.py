class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = collections.Counter(nums)
        keys = list(count.keys())
        keys.sort(key=lambda x: count[x], reverse=True)
        return keys[:k]
        