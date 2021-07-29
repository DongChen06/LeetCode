class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        dp = [1]

        for i in range(numRows - 1):
            dp_new = [0] + dp + [0]
            dp = []
            for i in range(len(dp_new) - 1):
                dp.append(dp_new[i] + dp_new[i + 1])
            out.append(dp)
        return out