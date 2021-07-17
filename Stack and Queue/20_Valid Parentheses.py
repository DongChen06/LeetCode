class Solution:
    def isValid(self, s: str) -> bool:

        opening = "({["
        stack = []

        for p in s:
            if p in opening:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False

                last_one = stack.pop()
                if last_one + p != '()' and last_one + p != '{}' and last_one + p != '[]':
                    return False

        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("{()}"))
