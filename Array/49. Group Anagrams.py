class Solution:
    def groupAnagrams(self, strs):
        adict = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in adict:
                adict[key].append(string)
            else:
                adict[key] = [string]
        return list(adict.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
