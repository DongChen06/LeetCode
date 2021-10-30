# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS, O(N), O(N)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res = []
        queue = collections.deque([root])

        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return res