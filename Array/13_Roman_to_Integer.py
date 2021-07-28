class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        out = 0
        l = len(s)
        for i in range(l):
            if i < l - 1:
                if roman[s[i]] < roman[s[i + 1]]:
                    out -= roman[s[i]]
                else:
                    out += roman[s[i]]
            else:
                out += roman[s[i]]

        return out

s = Solution()
print(s.romanToInt("MCMXCIV"))