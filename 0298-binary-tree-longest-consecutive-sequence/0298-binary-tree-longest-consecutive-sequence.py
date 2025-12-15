# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, parent, length):
            if not node:
                return
            
            if node.val == parent + 1:
                length += 1
            else:
                length = 1

            self.ans = max(self.ans, length)

            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)

        dfs(root, float('-inf'), 0)
        return self.ans   
        