# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.nodes = []
        self.in_oder_traverse(root)

    def in_oder_traverse(self, node):
        if not node:
            return
        self.in_oder_traverse(node.left)
        self.nodes.append(node.val)
        self.in_oder_traverse(node.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()