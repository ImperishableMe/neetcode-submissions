# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        node = TreeNode(val=preorder[0])
        where = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                where = i
                break
        node.left = self.buildTree(preorder[1: where + 1], inorder[:where])
        node.right = self.buildTree(preorder[where + 1: ], inorder[where + 1:])
        return node