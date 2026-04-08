class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)

        for _ in range(volume):
            best = k
            i = k
            while i > 0 and heights[i] >= heights[i - 1]:
                i -= 1
                if heights[i] < heights[best]:
                    best = i
            
            if best != k:
                heights[best] += 1
                continue

            best = k
            i = k
            while i < n - 1 and heights[i] >= heights[i + 1]:
                i += 1
                if heights[i] < heights[best]:
                    best = i

            heights[best] += 1

        return heights