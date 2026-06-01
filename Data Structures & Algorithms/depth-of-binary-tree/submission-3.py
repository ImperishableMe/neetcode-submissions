# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        st = [(root, 1)]
        h = 0
        while st:
            cur, cur_h = st.pop()
            h = max(h, cur_h)
            if cur.left:
                st.append((cur.left, cur_h + 1))
            if cur.right:
                st.append((cur.right, cur_h + 1))

        return h