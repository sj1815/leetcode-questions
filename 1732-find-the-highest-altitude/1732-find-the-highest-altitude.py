class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = highest_altitude = 0

        for alt_gain in gain:  
            current_altitude += alt_gain
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude