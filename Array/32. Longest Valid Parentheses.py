class Solution:
    # O(N), O(N)
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res


s = Solution()
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses("()(()"))
