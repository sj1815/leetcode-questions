class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def shoe_lace(p1, p2, p3):
            return 0.5 * abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            )

        n = len(points)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(max_area, shoe_lace(points[i], points[j], points[k]))
        return max_area
        