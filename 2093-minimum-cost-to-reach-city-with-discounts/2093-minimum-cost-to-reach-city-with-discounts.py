class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, cost in highways:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        dist = [[float('inf')] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            cost, city, used = heapq.heappop(pq)

            if cost > dist[city][used]:
                continue

            if city == n - 1:
                return cost

            for neighbor, price in graph[city]:
                new_cost = cost + price

                if new_cost < dist[neighbor][used]:
                    dist[neighbor][used] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, used))

                if used < discounts:
                    new_cost = cost + price // 2

                    if new_cost < dist[neighbor][used + 1]:
                        dist[neighbor][used + 1] = new_cost
                        heapq.heappush(
                            pq, (new_cost, neighbor, used + 1)
                        )

        return -1