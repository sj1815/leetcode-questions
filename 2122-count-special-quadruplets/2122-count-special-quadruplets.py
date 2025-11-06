class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        freq = defaultdict(int)
        
        for c in range(n - 2, 1, -1):
            freq[nums[c + 1]] += 1
            for a in range(c):
                for b in range(a + 1, c):
                    target = nums[a] + nums[b] + nums[c]
                    ans += freq[target]
        return ans
        