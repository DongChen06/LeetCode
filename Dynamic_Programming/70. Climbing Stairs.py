class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1 for i in range(n)]

        for i in range(1, n):
            if i == 1:
                steps[i] = 2
            else:
                steps[i] = steps[i - 1] + steps[i - 2]

        return steps[-1]

s = Solution()
print(s.climbStairs(3))
