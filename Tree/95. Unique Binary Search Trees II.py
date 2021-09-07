# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache


# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         @cache
#         def dfs(left, right):
#             if left < right:
#                 return [TreeNode(root, leftNode, rightNode)
#                         for root in range(left, right+1)
#                         for leftNode in dfs(left, root-1) for rightNode in dfs(root+1, right)]
#             elif left != right:
#                 return [None]
#             else:
#                 return [TreeNode(left)]

#         return dfs(1, n)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def rec(start, end):
            if start > end:
                return [None]

            if start == end:
                return [TreeNode(start)]
            ret_list = []

            for i in range(start, end + 1):
                left = rec(start, i - 1)
                right = rec(i + 1, end)
                for pair in product(left, right):
                    ret_list.append(TreeNode(i, pair[0], pair[1]))

            return ret_list

        res = rec(1, n)
        return res
