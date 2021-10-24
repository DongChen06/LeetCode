class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isvalidPalindrome(left, right, s, count):
            while left <= right:
                if s[left] != s[right]:
                    if count == 1:
                        return False
                    return isvalidPalindrome(left + 1, right, s, count + 1) or isvalidPalindrome(left, right - 1, s,
                                                                                                 count + 1)

                left += 1
                right -= 1

            return True

        return isvalidPalindrome(0, len(s) - 1, s, 0)