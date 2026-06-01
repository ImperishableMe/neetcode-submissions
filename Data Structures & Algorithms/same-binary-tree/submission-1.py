# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if (p is None or q is None):
                if p is not q:
                    return False
            else:        
                if p.val != q.val:
                    return False
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        
        return True
            