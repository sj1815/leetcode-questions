class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        points1 = []
        points2 = []

        n = len(img1)

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))
                if img2[r][c] == 1:
                    points2.append((r, c))

        count = {}
        ans = 0

        for r1, c1 in points1:
            for r2, c2 in points2:
                shift = (r2 - r1, c2 - c1)

                count[shift] = count.get(shift, 0) + 1
                ans = max(ans, count[shift])

        return ans