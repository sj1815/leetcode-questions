class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        unique_nums = []
        for num, count in freq.items():
            if count == 1:
                unique_nums.append(num)

        return max(unique_nums) if unique_nums else - 1

        