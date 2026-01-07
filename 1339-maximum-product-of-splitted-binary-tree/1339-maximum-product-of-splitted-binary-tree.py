# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        totals = []

        def dfs(node):
            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            totals.append(total_sum)
            return total_sum

        total = dfs(root)
        best = 0
        for s in totals:
            best = max(best, s * (total - s))
        return best % (10 ** 9 + 7)  
        