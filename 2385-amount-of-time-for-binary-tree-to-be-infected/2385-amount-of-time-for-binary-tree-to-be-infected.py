# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def build(node, parent):
            if not node:
                return
            
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build(node.left, node)
            build(node.right, node)

        build(root, None)

        infected = set([start])
        q = deque([start])
        time = -1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for nei in graph[curr]:
                    if nei not in infected:
                        infected.add(nei)
                        q.append(nei)
            time += 1

        return time
