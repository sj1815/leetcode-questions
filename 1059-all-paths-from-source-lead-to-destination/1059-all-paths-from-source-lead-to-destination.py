class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        state = [0] * n  #

        def dfs(node):
            if not graph[node]:
                return node == destination

            if state[node] == 1:
                return False  
            if state[node] == 2:
                return True   

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        return dfs(source)