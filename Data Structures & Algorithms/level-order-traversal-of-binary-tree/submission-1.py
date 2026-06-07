# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_nodes = []
        q = deque([root])
        while q:
            level_size = len(q)
            level_nodes.append([])
            for _ in range(level_size):
                cur_node = q.popleft()
                level_nodes[-1].append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        return level_nodes