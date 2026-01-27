class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_mat = [[] for _ in range(n)]
        for x, y, z in edges:
            adj_mat[x].append((y, z))
            adj_mat[y].append((x, 2 * z))

        dist = [inf] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            if visited[x]:
                continue
            visited[x] = True

            for y, z in adj_mat[x]:
                new_dist = cur_dist + z
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))

        return -1
        