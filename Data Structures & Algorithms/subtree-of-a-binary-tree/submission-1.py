# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root is subRoot

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))
    
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root is subRoot
        return (
            root.val == subRoot.val and
            self.isSame(root.left, subRoot.left) and
            self.isSame(root.right, subRoot.right)
        )
