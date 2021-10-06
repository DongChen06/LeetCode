class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res, shift = '', 0

        for i in range(len(shifts) - 1, -1, -1):
            letter = s[i]
            shift += shifts[i]
            res += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

        return res[::-1]