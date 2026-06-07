# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_th, count = None, 0
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            nonlocal count, k_th
            count += 1
            if count == k:
                k_th = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return k_th