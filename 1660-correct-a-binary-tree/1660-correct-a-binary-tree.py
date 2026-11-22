# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        visited = set()

        def build_correct_tree(node):
            if node is None:
                return None

            if node.right and node.right.val in visited:
                return None
            
            visited.add(node.val)

            node.right = build_correct_tree(node.right)
            node.left = build_correct_tree(node.left)

            return node
        
        return build_correct_tree(root)