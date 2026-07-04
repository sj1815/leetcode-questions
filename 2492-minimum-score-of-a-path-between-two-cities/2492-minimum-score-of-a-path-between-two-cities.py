class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visited = set()
        q = deque([1])
        visited.add(1)

        ans = float('inf')

        while q:
            node = q.popleft()

            for nei, wt in adj[node]:
                ans = min(ans, wt)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans