class Solution:
    # O(N), O(N - D)
    def removeDuplicates(self, s: str) -> str:
        res = []
        for si in s:
            if res and res[-1] == si:
                res.pop()
            else:
                res.append(si)

        return "".join(res)