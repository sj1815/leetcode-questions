class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = (set(range(1, n+1)) - seen).pop()
        return [duplicate, missing]
        