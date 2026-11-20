class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        def helper(L, M):
            n = len(nums)

            left = sum(nums[:L])
            right = sum(nums[L:L + M])

            maxLeft = left
            ans = left + right

            for i in range(L + M, n):

                # Slide left window
                left += nums[i - M] - nums[i - M - L]

                # Slide right window
                right += nums[i] - nums[i - M]

                # Keep maximum valid left window
                maxLeft = max(maxLeft, left)

                ans = max(ans, maxLeft + right)

            return ans

        return max(
            helper(firstLen, secondLen),
            helper(secondLen, firstLen)
        )