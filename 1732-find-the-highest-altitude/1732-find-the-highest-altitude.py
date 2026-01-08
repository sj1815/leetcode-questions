class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = highest_alt = 0

        for alt_gain in gain:
            current_alt += alt_gain
            highest_alt = max(highest_alt, current_alt)
        
        return highest_alt