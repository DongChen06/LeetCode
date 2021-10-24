class Solution:
    # O(N*M), O(N*M)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        res = []

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,  # up
                                   dfs(i + 1, j) if i + 1 < row and val > matrix[i + 1][j] else 0,  # down
                                   dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,  # left
                                   dfs(i, j + 1) if j + 1 < col and val > matrix[i][j + 1] else 0)  # down

            return dp[i][j]

        for i in range(row):
            for j in range(col):
                res.append(dfs(i, j))
        return max(res)