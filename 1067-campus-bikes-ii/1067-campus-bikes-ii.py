class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        used = [False] * m
        self.best = float("inf")

        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])

        def backtrack(i, total):
            if i == n:
                self.best = min(self.best, total)
                return

            if total >= self.best:
                return

            for j in range(m):
                if not used[j]:
                    used[j] = True
                    backtrack(i + 1, total + dist(i, j))
                    used[j] = False   

        backtrack(0, 0)
        return self.best

        