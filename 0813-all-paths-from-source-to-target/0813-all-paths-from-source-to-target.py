class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        res = []

        def backtrack(curr, path):
            if curr == n:
                res.append(list(path))
                return
            for node in graph[curr]:
                path.append(node)
                backtrack(node, path)
                path.pop()
            

        backtrack(0, [0])
        return res
        
