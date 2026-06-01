# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # height is considered in edge
        stack = [(root, True)] # tuples (node, is first visit (two visits for each node)) 
        res = 0
        node_height = defaultdict(int)
        while stack:
            cur, first = stack.pop()
            #print(cur.val)
            if not cur:
                continue
            if first:
                stack.append((cur, False))
                stack.append((cur.left, True))
                stack.append((cur.right, True))
            else:
                node_height[cur] = max(node_height[cur.left], node_height[cur.right]) + 1
                res = max(res, node_height[cur.left] + node_height[cur.right])
                
        return res