from sortedcontainers import SortedList

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        n = len(self.bit)
        while i < n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries):
        MAX = min(50000, len(queries) * 3)

        obstacles = SortedList([0, MAX])

        # Insert all obstacles first
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = Fenwick(MAX + 2)

        # Build initial gaps
        for i in range(len(obstacles) - 1):
            a = obstacles[i]
            b = obstacles[i + 1]
            bit.update(b, b - a)

        ans = []

        # Process in reverse
        for q in reversed(queries):

            if q[0] == 1:
                x = q[1]

                idx = obstacles.index(x)
                prev = obstacles[idx - 1]
                nxt = obstacles[idx + 1]

                obstacles.remove(x)

                # merged interval
                bit.update(nxt, nxt - prev)

            else:
                x, sz = q[1], q[2]

                idx = obstacles.bisect_right(x)
                prev = obstacles[idx - 1]

                ok = (
                    bit.query(prev) >= sz or
                    x - prev >= sz
                )

                ans.append(ok)

        return ans[::-1]