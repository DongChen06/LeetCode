class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ispositive = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        the_sum = divisor
        res = 0

        while the_sum <= dividend:
            current_q = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                current_q += current_q

            dividend -= the_sum
            the_sum = divisor
            res += current_q

        return min(2 ** 31 - 1, max(-2 ** 31, res if ispositive else -res))