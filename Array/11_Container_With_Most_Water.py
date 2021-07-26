class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1

        out = float('-inf')

        while i < j:
            left, right = height[i], height[j]
            out = max(out, min(left, right) * (j - i))

            if left < right:
                i += 1
            else:
                j -= 1
        return out