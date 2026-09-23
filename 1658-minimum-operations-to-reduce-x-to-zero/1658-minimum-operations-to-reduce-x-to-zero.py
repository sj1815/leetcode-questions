class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        current = sum(nums)
        n = len(nums)
        mini = inf
        left = 0

        for right in range(n):
            current -= nums[right]
            while current < x and left <= right:
                current += nums[left]
                left += 1
            if current == x:
                mini = min(mini, (n-1-right)+left)

        return mini if mini != inf else -1