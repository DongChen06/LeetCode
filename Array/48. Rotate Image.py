class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        n1 = n - 1
        for i in range(n // 2):
            for j in range(n1 - 2 * i):
                (matrix[i][i + j], matrix[i + j][n1 - i],
                 matrix[n1 - i][n1 - i - j],
                 matrix[n1 - i - j][i]) = (matrix[n1 - i - j][i], matrix[i][i + j],
                                      matrix[i + j][n1 - i], matrix[n1 - i][n1 - i - j])