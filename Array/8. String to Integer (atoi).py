class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        out = ''
        positive = True
        start = False
        leading_zero = True

        for c in s:
            if c == ' ' and start == False:
                continue
            elif c == '-' and start == False:
                positive = False
                start = True
                leading_zero = False
            elif c == '+' and start == False:
                start = True
                leading_zero = False
            elif c not in digits:
                break
            elif c in digits:
                start = True
                if c == '0' and leading_zero == True:
                    continue
                else:
                    leading_zero = False
                    out += c

        if out == '':
            return 0

        if positive:
            return int(out) if int(out) <= 2 ** 31 - 1 else 2 ** 31 - 1
        else:
            return -int(out) if -int(out) >= -2 ** 31 else -2 ** 31

