# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_map = []

        # pre-order traverse
        def preoder_traverse(node, col, row):
            if not node:
                return
            node_map.append((col, row, node.val))
            preoder_traverse(node.left, col - 1, row + 1)
            preoder_traverse(node.right, col + 1, row + 1)

        preoder_traverse(root, 0, 0)

        res = [[]]
        node_map.sort()
        min_col = node_map[0][0]

        for col, row, val in node_map:
            if col != min_col:
                res.append([])

            res[-1].append(val)
            min_col = col

        return res