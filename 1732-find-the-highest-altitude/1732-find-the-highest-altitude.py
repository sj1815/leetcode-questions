class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = highest_alt = 0
        
        for alt_gain in gain:
            curr_alt += alt_gain
            hightest_alt = max(highest_alt, curr_alt)

        return highest_alt