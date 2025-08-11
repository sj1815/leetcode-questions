# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, direction, length):
            if not node:
                return
            self.max_len = max(self.max_len, length)
            if direction == 0:  # last move was left, so now go right
                dfs(node.right, 1, length + 1)  # continue zigzag
                dfs(node.left, 0, 1)  # restart if same direction
            else:  # last move was right, so now go left
                dfs(node.left, 0, length + 1)
                dfs(node.right, 1, 1)

        dfs(root.left, 0, 1)  # start by going left
        dfs(root.right, 1, 1) # start by going right
        return self.max_len