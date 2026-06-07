# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, -10**9)]
        res = 0
        while stack:
            node, max_ancestor = stack.pop()
            if not node:
                continue
            res += 1 if node.val >= max_ancestor else 0
            max_ancestor = max(max_ancestor, node.val)
            stack.append((node.left, max_ancestor))
            stack.append((node.right, max_ancestor))
        
        return res