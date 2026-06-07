# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root: Optional[TreeNode], path: list[str]) -> list[str]:
        if not root:
            return path

        path.append(str(root.val))

        if root.left:
            self.serialize(root.left, path)
        else:
            path.append('#')
        
        if root.right:
            self.serialize(root.right, path)
        else:
            path.append('#')
        return path

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_serialized = ''.join(self.serialize(root, []))
        sub_root_serialized = ''.join(self.serialize(subRoot, []))
        return sub_root_serialized in root_serialized
        
        if not root or not subRoot:
            return root is subRoot

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))
    
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root is subRoot
        return (
            root.val == subRoot.val and
            self.isSame(root.left, subRoot.left) and
            self.isSame(root.right, subRoot.right)
        )
