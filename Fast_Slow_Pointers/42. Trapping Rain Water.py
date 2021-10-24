class Solution:
    # O(N), O(N)
    def trap(self, height: List[int]) -> int:
        leftmax = [height[0] for _ in range(len(height))]
        rightmax = [height[-1] for _ in range(len(height))]
        res = 0

        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i - 1], height[i - 1])

        for j in range(len(height) - 2, -1, -1):
            rightmax[j] = max(rightmax[j + 1], height[j + 1])

        for z in range(len(height) - 2, -1, -1):
            if min(leftmax[z], rightmax[z]) - height[z] > 0:
                res += min(leftmax[z], rightmax[z]) - height[z]

        return res


class Solution1:
    # two pointers: O(N), O(1)
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        rightmax = height[-1]
        res, l, r = 0, 0, len(height) - 1

        while l < r:
            if leftmax <= rightmax:
                l += 1
                res += leftmax - height[l] if leftmax - height[l] > 0 else 0
                leftmax = max(leftmax, height[l])
            else:
                r -= 1
                res += rightmax - height[r] if rightmax - height[r] > 0 else 0
                rightmax = max(rightmax, height[r])
        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
