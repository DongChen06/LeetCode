class Solution:
    # monotonic decreasing queue. O(N), O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left, right = 0, 0
        q = collections.deque()

        while right < len(nums):
            # pop smaller value from q
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            q.append(right)
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1

            right += 1
        return res
