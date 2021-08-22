class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10

        res, zero = res[::-1], 0
        while zero < len(res) and res[zero] == 0:
            zero += 1

        res = map(str, res[zero:])
        return "".join(res)


s = Solution()
print(s.multiply("123", "456"))
