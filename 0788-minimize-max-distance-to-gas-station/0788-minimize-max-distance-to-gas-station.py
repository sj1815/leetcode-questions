class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # HEAP(EXCEEDED TIME)
        # hp = []
        # for i in range(len(stations) - 1):
        #     x, y = stations[i], stations[i + 1]
        #     hp.append((x - y, y - x, 1))
        # heapq.heapify(hp)

        # for _ in range(k):
        #     _, num, den = heapq.heappop(hp)
        #     den += 1
        #     heapq.heappush(hp, (-(num / den), num, den))
        # return -hp[0][0]
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= k

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo
        