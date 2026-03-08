class LogSystem:

    def __init__(self):
        self.logs = []
        self.gra = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = []
        idx = self.gra[granularity]

        start = start[:idx]
        end = end[:idx]

        for ts, id in self.logs:
            if start <= ts[:idx] <= end:
                res.append(id)

        return res
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)