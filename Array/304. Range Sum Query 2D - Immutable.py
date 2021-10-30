class NumMatrix:
    # smart storage, O(1), pre-compute O(nm), O(mn)
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                left = self.dp[i][j-1] if j > 0 else 0
                top = self.dp[i - 1][j] if i > 0 else 0
                topleft = self.dp[i-1][j-1] if (i > 0 and j > 0) else 0
                self.dp[i][j] = matrix[i][j] + left + top - topleft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.dp[row2][col1 -1] if col2 > 0 else 0
        top = self.dp[row1 - 1][col2]  if row1 > 0 else 0
        topleft = self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.dp[row2][col2] + topleft - left - top

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)