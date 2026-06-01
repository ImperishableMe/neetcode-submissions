# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # returns (height, isBalanced) for root 
        def dfs(root) -> Tuple[int, bool]:
            if not root:
                return 0, True
            left_height, left_balanced = dfs(root.left)
            right_height, right_balanced = dfs(root.right)

            return (
                max(left_height, right_height) + 1,
                all((left_balanced, right_balanced,
                    abs(left_height - right_height) <= 1))
            )

        return dfs(root)[1]