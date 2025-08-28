class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        max_frequency = 0
        for num in counts.keys():
            max_gain = 0
            current_sum = 0
            for n in nums:
                if n == k:
                    current_sum -= 1
                elif n == num:
                    current_sum += 1
                if current_sum < 0:
                    current_sum = 0
                max_gain = max(max_gain, current_sum)
            max_frequency = max(max_frequency, max_gain)
        return counts[k] + max_frequency
        