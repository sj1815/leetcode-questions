class RecentCounter:

    def __init__(self):
        self.calls = collections.deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)

        while self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(calls)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)