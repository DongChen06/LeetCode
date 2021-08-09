class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ""

        for index, s in enumerate(strs):
            if s == "":
                prefix = ""
                break
            else:
                if index == 0:
                    prefix = s
                else:
                    prefix = prefix if len(prefix) < len(s) else prefix[:len(s)]
                    for i in range(min(len(prefix), len(s))):
                        if prefix[i] != s[i]:
                            prefix = prefix[:i]
                            break

        return prefix

s = Solution()
print(s.longestCommonPrefix(["ab", "a"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
