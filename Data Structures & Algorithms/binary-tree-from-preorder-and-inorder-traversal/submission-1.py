# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # where = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        where = {}
        for i, val in enumerate(inorder):
            where[val] = i
        pre = 0

        def build(left: int, right: int) -> TreeNode:
            nonlocal pre
            if left > right:
                return None
            
            node = TreeNode(val=preorder[pre])
            cur_pos = where[preorder[pre]]
            pre += 1
            node.left = build(left, cur_pos - 1)
            node.right = build(cur_pos + 1, right)
            return node

        return build(0, len(preorder) - 1)