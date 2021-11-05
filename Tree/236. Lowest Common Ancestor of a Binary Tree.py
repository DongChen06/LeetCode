# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __int__(self, ):
        self.res = None

    # dfs, O(N), O(N)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(node):
            if not node:
                return False

            left = traverse(node.left)
            right = traverse(node.right)
            mid = node == p or node == q

            if mid + left + right >= 2:
                self.res = node

            return mid or left or right

        traverse(root)
        return self.res