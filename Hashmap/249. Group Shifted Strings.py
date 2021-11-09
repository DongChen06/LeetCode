class Solution:
    # O(ab), O(n)
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                order = 26 + ord(s[i + 1]) - ord(s[i])
                key += (order % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]

        return list(hashmap.values())