class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_points = sum(cardPoints)

        if k == n:
            return total_points

        window = n - k
        curr_sum = sum(cardPoints[:window])
        min_window_sum = curr_sum

        for i in range(window, n):
            curr_sum += cardPoints[i]
            curr_sum -= cardPoints[i - window]
            min_window_sum = min(min_window_sum, curr_sum)

        return total_points - min_window_sum
