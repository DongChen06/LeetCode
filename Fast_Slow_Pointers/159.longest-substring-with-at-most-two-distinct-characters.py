# Time:  O(n)
# Space: O(1)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end, max_len = 0, 0, 0
        d = {}

        for end, si in enumerate(s):
            d[si] = end
            if len(d) > 2:
                min_idx = min(d.values())
                start = min_idx + 1
                del d[s[min_idx]]
            max_len = max(max_len, end - start + 1)

        return max_len


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eceba"))  # 3
print(s.lengthOfLongestSubstringTwoDistinct("ccaabbb"))  # 5
print(s.lengthOfLongestSubstringTwoDistinct(""))
