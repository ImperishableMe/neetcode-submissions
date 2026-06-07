# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view: list[int] = []
        
        def dfs(node: Optional[TreeNode], depth: int = 0):
            if not node:
                return
            if len(right_view) == depth:
                right_view.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root)
        return right_view