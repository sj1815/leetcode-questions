class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        ops = 0

        for num in nums:
            compliment = k - num
            if count[compliment] > 0:
                ops += 1
                count[compliment] -= 1
            else:
                count[num] += 1

        return ops
        
