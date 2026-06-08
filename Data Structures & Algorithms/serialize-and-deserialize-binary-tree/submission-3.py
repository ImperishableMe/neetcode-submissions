# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        codes = []
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                codes.append('#')
                continue
            codes.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        while codes and codes[-1] == '#':
            codes.pop()

        return ','.join(codes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(data)
        if data == '':
            return None
        codes = data.split(',')
        # print(f"hello {codes}")
        n = len(codes)
        pos = 0
        
        root = TreeNode(int(codes[pos]))
        q = deque([root])
        while q:
            node = q.popleft()
            pos += 1
            if pos < n and codes[pos] != '#':
                node.left = TreeNode(int(codes[pos]))
                q.append(node.left)
            pos += 1
            if pos < n and codes[pos] != '#':
                node.right = TreeNode(int(codes[pos]))
                q.append(node.right)
        
        return root
