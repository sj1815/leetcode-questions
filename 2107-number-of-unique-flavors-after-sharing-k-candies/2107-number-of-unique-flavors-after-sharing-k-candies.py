class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        flav_freq = defaultdict(int)
        for c in candies:
            flav_freq[c] += 1

        unique_flav = len(flav_freq)

        used_in_window = 0
        for i in range(k):
            flav_freq[candies[i]] -= 1
            if flav_freq[candies[i]] == 0:
                used_in_window += 1

        max_flav = unique_flav - used_in_window

        for i in range(k, len(candies)):
            flav_freq[candies[i - k]] += 1
            if flav_freq[candies[i - k]] == 1:
                used_in_window -= 1

            flav_freq[candies[i]] -= 1
            if flav_freq[candies[i]] == 0:
                used_in_window += 1

            max_flav = max(max_flav, unique_flav - used_in_window)

        return max_flav