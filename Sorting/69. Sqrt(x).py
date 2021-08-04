class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        if x == 0:
            return x

        left = 1
        right = x

        while left < right - 1:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid
            else:
                right = mid

        return left


s = Solution()
print(s.mySqrt(8))