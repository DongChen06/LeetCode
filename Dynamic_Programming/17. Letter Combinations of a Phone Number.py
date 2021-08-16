class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2letter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        out = []

        # base case
        if digits == "":
            return []

        else:
            for s in digits:
                if not out:
                    out = num2letter[s]
                else:
                    out = [i + j for i in out for j in num2letter[s]]
        return out