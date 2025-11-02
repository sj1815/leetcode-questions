class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = min_prod = res = nums[0]

        for n in nums[1:]:
            if n < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(n, max_prod * n)
            min_prod = min(n, min_prod * n)

            res = max(res, max_prod)
        
        return res
