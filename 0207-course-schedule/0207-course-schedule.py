class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        status = [UNVISITED] * numCourses

        def dfs(node):
            s = status[node]
            if s == VISITED: return True
            elif s == VISITING: return False

            status[node] = VISITING

            for nei in g[node]:
                if not dfs(nei): return False
            
            status[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
        