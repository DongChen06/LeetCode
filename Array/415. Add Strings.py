class Solution:
    # O(max(N1, N2)), O(max(N1, N2))
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry = [], 0
        l1, l2 = len(num1) - 1, len(num2) - 1

        while l1 >= 0 or l2 >= 0:
            x1 = int(num1[l1]) if l1 >= 0 else 0
            x2 = int(num2[l2]) if l2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            l1, l2 = l1 - 1, l2 - 1

        if carry:
            res.append(carry)

        return "".join(str(x) for x in res[::-1])