class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        result = 0
        
        def dfs(node: int) -> int:
            nonlocal result
            visited[node] = True
            
            total = values[node] % k
            for nei in graph[node]:
                if not visited[nei]:
                    subtotal = dfs(nei)
                    total = (total + subtotal) % k
            
            if total == 0:
                result += 1
                return 0 
            
            return total
        
        dfs(0)
        return result
