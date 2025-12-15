class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()
        self.count = 0

        def dfs(city):
            visited.add(city)
            for nei, reverse in graph[city]:
                if nei not in visited:
                    self.count += reverse
                    dfs(nei)
            

        dfs(0)
        return self.count