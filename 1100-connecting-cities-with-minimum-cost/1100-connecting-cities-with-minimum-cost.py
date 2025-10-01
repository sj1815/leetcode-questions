class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = {i :[] for i in range(1, n + 1)}
        for u, v, cost in connections:
            graph[u].append((cost, v))
            graph[v].append((cost, u))
            
        visited = set()
        min_heap = [(0, 1)]  
        total_cost = 0

        while min_heap and len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost
            for next_cost, v in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (next_cost, v))

        return total_cost if len(visited) == n else -1
            