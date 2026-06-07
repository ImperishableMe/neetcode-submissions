# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_nodes = [] # List[List[int]]

        def dfs(root: TreeNode, h: int):
            nonlocal level_nodes
            if not root:
                return
            if len(level_nodes) == h:
                level_nodes.append([])

            level_nodes[h].append(root.val)

            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
        
        dfs(root, 0)

        return level_nodes
            
