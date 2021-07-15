class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        num = 0

        for i in range(l):
            num += digits[i] * 10 ** (l - i - 1)

        num_new = num + 1

        out = []

        for i in range(len(str(num_new))):
            out.append(int(str(num_new)[i]))

        return out