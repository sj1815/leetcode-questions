class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l = 0
        r = n - 1

        for i in range(n - 1,  -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                val = nums[r]
                r -= 1
            else:
                val = nums[l]
                l += 1
            ans[i] = val * val
        
        return ans
  