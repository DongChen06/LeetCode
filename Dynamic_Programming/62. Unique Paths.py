
# DP + memorization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        def path(m, n):

            if m == 1 or n == 1:
                dp[m][n] = 1
                return 1
            if dp[m][n]:
                return dp[m][n]

            dp[m][n] = path(m - 1, n) + path(m, n - 1)
            return dp[m][n]

        return path(m, n)