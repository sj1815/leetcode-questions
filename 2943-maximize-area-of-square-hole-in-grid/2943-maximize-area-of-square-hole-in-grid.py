class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longestConsecutive(bars):
            bars.sort()
            maxCount = count = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    count += 1
                else:
                    count = 1
                maxCount = max(maxCount, count)
            return maxCount

        maxH = longestConsecutive(hBars) if hBars else 0
        maxW = longestConsecutive(vBars) if vBars else 0

        side = min(maxH, maxW) + 1
        return side * side
        