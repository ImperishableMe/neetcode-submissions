# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
                2
                    4
             10         8
                    4
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        MIN_INF = -10**9
        def dfs(node: TreeNode, max_value: int) -> int:
            if not node:
                return 0
            good_count = 1 if node.val >= max_value else 0
            print(node.val, max_value, good_count)
            max_in_subtree = max(max_value, node.val)
            return (good_count +
                dfs(node.left, max_in_subtree) +
                dfs(node.right, max_in_subtree)
            )
        return dfs(root, MIN_INF)