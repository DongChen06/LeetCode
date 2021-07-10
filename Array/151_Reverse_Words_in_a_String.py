class Solution:
    def reverseWords(self, s: str) -> str:
        length = len(s)
        space = [' ']
        output = []
        outstring = ""
        i = 0
        while i < length:
            if s[i] not in space:
                word_start = i
                while s[i] not in space and i < length:
                    i += 1
                output.append(s[word_start:i])
            i += 1
        # return " ".join(reversed(output)
        
        for a in range(len(output)-1, -1, -1):
            if a != 0:
                outstring += output[a] + " "
            else:
                outstring += output[a]
        return outstring

s = "a good   example "
solution = Solution()
print(solution.reverseWords(s))