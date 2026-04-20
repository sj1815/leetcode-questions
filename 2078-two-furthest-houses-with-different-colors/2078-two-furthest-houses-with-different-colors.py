class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left, right = 0, n - 1

        while colors[right] == colors[0]:
            right -= 1

        while colors[left] == colors[n-1]:
            left += 1
            
        return max(right, n - 1 - left)