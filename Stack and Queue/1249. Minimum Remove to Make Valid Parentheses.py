class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid_closing(string, opening, closing):
            sv = []

            balance = 0
            for s in string:
                if s == opening:
                    balance += 1
                if s == closing:
                    if balance == 0:
                        continue
                    balance -= 1
                sv.append(s)
            return "".join(sv)

        sv = delete_invalid_closing(s, "(", ")")
        res = delete_invalid_closing(sv[::-1], ")", "(")
        return "".join(res[::-1])