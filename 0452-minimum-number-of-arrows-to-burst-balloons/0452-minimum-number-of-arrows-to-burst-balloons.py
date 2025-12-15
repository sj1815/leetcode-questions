class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key = lambda x : x[1])

        arrows = 1
        left = points[0][1]
        for start, right in points:
            if left < start:
                arrows += 1
                left = right

        return arrows
        