class Leaderboard:

    def __init__(self):
        self.scores: Dict[int, int] = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        if K <= 0:
            return 0
        top_k = heapq.nlargest(K, self.scores.values())
        return sum(top_k)

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)