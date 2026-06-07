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
        
        stack = [root]
        while stack:
            cur = stack.pop()
            if max(p.val, q.val) < cur.val:
                assert cur.left
                stack.append(cur.left)
            elif min(p.val, q.val) > cur.val:
                assert cur.right
                stack.append(cur.right)
            else:
                return cur

        return None