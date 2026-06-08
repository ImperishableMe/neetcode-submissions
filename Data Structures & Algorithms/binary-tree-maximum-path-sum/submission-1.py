# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')
       
        def dfs(node: Optional[TreeNode]) -> int:
            """
            returns maximum of left_down and right_down starting from `node`
            """
            nonlocal max_path_sum
            if not node:
                return 0
            
            left_down = max(dfs(node.left), 0)
            right_down = max(dfs(node.right), 0)
            max_from_node = left_down + right_down + node.val
            max_path_sum = max(max_path_sum, max_from_node)
            return max(left_down, right_down) + node.val
        
        dfs(root)
        return max_path_sum
