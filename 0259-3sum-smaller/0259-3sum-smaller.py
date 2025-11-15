class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < target:
                    count += (k - j)
                    j += 1
                else:
                    k -= 1

        return count