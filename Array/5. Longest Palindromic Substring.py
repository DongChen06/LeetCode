class Solution:
    def longestPalindrome(self, s: str) -> str:
        #         max_p = 1
        #         max_s = s[0]

        #         for i in range(len(s) - 1):
        #             for j in range(i+1, len(s)):
        #                 if s[i:j+1] == s[i:j+1][::-1] and j+1-i > max_p:
        #                     max_p = j+1-i
        #                     max_s = s[i:j+1]

        #         return max_s
        mylist = []
        for i in range(len(s)):
            pal = palexpand(s, i, i)
            pal1 = palexpand(s, i - 1, i)
            if pal != None:
                mylist.append(pal)
            if pal1 != None:
                mylist.append(pal1)
        return (max(sorted(mylist), key=len))


def palexpand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return (s[l + 1:r])