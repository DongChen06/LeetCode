class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        digits = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        out = ""

        for i in range(len(digits) - 1, -1, -1):
            count = num // digits[i]

            if count > 0:
                out += roman[i] * count
                num -= digits[i] * count

            if num == 0:
                break
        return out


s = Solution()
print(s.intToRoman(20))