# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # first root where p and q goes into different subtree
        if not root or not p or not q:
            return root
        
        if max(p.val, q.val) < root.val:
            assert root.left
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            assert root.right
            return self.lowestCommonAncestor(root.right, p, q)

        return root        