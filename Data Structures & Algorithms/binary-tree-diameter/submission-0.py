# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> tuple(int, int): # returns (max_diameter in subtree, max depth in subtree)
            if not root:
                return [0, 0]
            left_diameter, left_depth = dfs(root.left)
            right_diameter, right_depth = dfs(root.right)

            depth = max(left_depth, right_depth) + 1
            diameter = max(left_diameter, right_diameter, left_depth + right_depth)
            return diameter, depth

        return dfs(root)[0]