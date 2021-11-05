# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N), O(N)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l, h = low, high
        res = []

        def dfs(node):
            if not node:
                return

            if node.val < l:
                dfs(node.right)
            elif node.val >= l and node.val <= h:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)
        return sum(res)
