"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        first, last = None, None

        def helper(node):
            nonlocal first, last
            # in-order traversal
            if not node:
                return

            helper(node.left)

            if last:
                node.left = last
                last.right = node
            else:
                first = node
            last = node

            helper(node.right)

        helper(root)
        last.right = first
        first.left = last
        return first