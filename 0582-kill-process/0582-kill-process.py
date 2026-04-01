class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)
        
        result = []
        
        def dfs(node):
            result.append(node)
            for child in tree[node]:
                dfs(child)
        
        dfs(kill)
        return result