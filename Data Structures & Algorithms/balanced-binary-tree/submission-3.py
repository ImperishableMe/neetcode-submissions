# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height = defaultdict(int)
        stack = [root]

        while stack:
            cur = stack[-1]
            done = True
            if cur.left and cur.left not in height:
                stack.append(cur.left)
                done = False
            if cur.right and cur.right not in height:
                stack.append(cur.right)
                done = False

            if not done:
                continue
            stack.pop()
            if abs(height[cur.left] - height[cur.right]) > 1:
                return False
            height[cur] = max(height[cur.left], height[cur.right]) + 1

            if cur.left in height:
                del height[cur.left]    
            if cur.right in height:
                del height[cur.right]

        return True
