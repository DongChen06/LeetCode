class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = []
        maxl = 0

        for si in s:
            if si not in out:
                out.append(si)
            else:
                if len(out) > maxl:
                    maxl = len(out)
                out = out[out.index(si) + 1:] + [si]
        return max(maxl, len(out))

        # max_len = 0
        # temp = ""
        # for x in s:
        #     if x in temp:
        #         max_len = max(max_len, len(temp))
        #         temp = temp[temp.find(x) + 1:]
        #     temp += x
        # return max(max_len, len(temp))

s = Solution()
print(s.lengthOfLongestSubstring(" "))