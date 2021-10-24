# Definition for a node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoubly(self, root):

        def inorder_traverse(node):
            nonlocal head, tail
            if not node:
                return
            inorder_traverse(node.left)
            # self
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node
            tail = node
            inorder_traverse(node.right)

        head, tail = None, None
        inorder_traverse(root)

        head.left, tail.left = tail, head
        return head
