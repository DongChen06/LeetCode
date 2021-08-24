# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, minValue=float(-inf), maxValue=float(inf)) -> bool:
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        return self.isValidBST(root.left, minValue, root.val) and self.isValidBST(root.right, root.val, maxValue)