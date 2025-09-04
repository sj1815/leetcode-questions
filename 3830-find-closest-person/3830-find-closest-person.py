class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist_xz, dist_yz = abs(z - x), abs(z - y)
        if dist_xz == dist_yz:
            return 0
        elif dist_xz < dist_yz:
            return 1
        else:
            return 2
        