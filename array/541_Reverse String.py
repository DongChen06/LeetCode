class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = ''

        if len(s) < k:
            out = s[::-1]
        elif k <= len(s) and len(s) < 2 * k:
            out = s[:k][::-1] + s[k:]
        else:
            i = 0
            while (2 * i + k) <= len(s) and (2 * i + 2 * k) <= len(s):
                out += s[(2 * i): (2 * i + k)][::-1] + s[(2 * i + k): (2 * i + 2 * k)]
                i += k
            if (2 * i + k) <= len(s) and (2 * i + 2 * k) > len(s):
                out += s[(2 * i): (2 * i + k)][::-1] + s[(2 * i + k):]
            if (2 * i + k) > len(s):
                out += s[(2 * i):][::-1]
        return out


s = Solution()
# input = "abcdefg"
# k = 2
# print(s.reverseStr(input, k))
# print(s.reverseStr("abcd", 3))
print(s.reverseStr("abcdefg", 3))
