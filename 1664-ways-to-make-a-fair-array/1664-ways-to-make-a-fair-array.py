class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right_even = right_odd = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even += num
            else:
                right_odd += num

        left_even = left_odd = 0
        res = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num

            if left_even + right_odd == right_even + left_odd:
                res += 1

            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        
        return res