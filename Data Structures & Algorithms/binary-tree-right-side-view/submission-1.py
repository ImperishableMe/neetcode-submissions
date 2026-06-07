# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_view = []
        q = deque([root])
        while q:
            level_size = len(q)
            right_view.append(q[0].val)
            for _ in range(level_size):
                cur_node = q.popleft()
                # if len(level_nodes[-1].append(cur_node.val)
                if cur_node.right:
                    q.append(cur_node.right)
                if cur_node.left:
                    q.append(cur_node.left)
                
        return right_view