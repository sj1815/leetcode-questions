class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        dp = [float('inf')] * n
        next_index = [-1] * n

        # You can’t land on blocked positions (-1)
        if coins[-1] == -1:
            return []

        dp[-1] = coins[-1]

        # Fill DP from the end backwards
        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue  # can't step here
            for j in range(i + 1, min(i + maxJump + 1, n)):
                if dp[j] == float('inf'):
                    continue
                new_cost = coins[i] + dp[j]
                if new_cost < dp[i]:
                    dp[i] = new_cost
                    next_index[i] = j

        # If we never found a valid path from index 0
        if dp[0] == float('inf'):
            return []

        # Reconstruct path from 0 using next_index
        path = []
        i = 0
        while i != -1:
            path.append(i + 1)  # convert to 1-based index
            i = next_index[i]

        return path