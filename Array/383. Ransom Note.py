class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_n = collections.Counter(ransomNote)
        count_m = collections.Counter(magazine)

        for s in count_n.keys():
            if s not in count_m or count_n[s] > count_m[s]:
                return False

        return True