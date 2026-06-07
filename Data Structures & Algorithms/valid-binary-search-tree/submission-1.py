# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        def dfs(node: TreeNode, value_range: Tuple[int, int]) -> bool:
            if not node:
                return True
            l, r = value_range
            if not (l <= node.val <= r):
                return False
            return (
                dfs(node.left, (l, node.val - 1)) and
                dfs(node.right, (node.val + 1, r))
            )
        return dfs(root, (-10**9, 10**9))
