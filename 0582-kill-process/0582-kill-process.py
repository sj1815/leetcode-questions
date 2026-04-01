class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        res = []

        for child, parent in zip(pid, ppid):
            tree[parent].append(child)

        def dfs(node):
            res.append(node)
            for child in tree[node]:
                dfs(child)
        
        dfs(kill)
        return res