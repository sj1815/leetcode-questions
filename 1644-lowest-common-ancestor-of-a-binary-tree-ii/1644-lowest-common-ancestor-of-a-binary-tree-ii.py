class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.found = set()

        def dfs(node):
            if not node:
                return None

            if node == p:
                self.found.add(p)
            elif node == q:
                self.found.add(q)

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                return node

            if left and right:
                return node

            return left or right

        ans = dfs(root)

        return ans if len(self.found) == 2 else None