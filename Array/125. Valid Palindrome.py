class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_s = ''

        for c in s:
            if c.isalnum():
                filter_s += c

        filter_s = filter_s.lower()
        left, right = 0, len(filter_s) - 1

        while left < right:
            if filter_s[left] != filter_s[right]:
                return False

            left += 1
            right -= 1

        return True