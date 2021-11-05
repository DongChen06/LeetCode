class Solution:
    # log(n), log(n)
    def myPow(self, x: float, n: int) -> float:

        def fpow(a, b):
            if b == 0:
                return 1

            half = fpow(a, b // 2)
            if b % 2 == 0:
                return half * half
            else:
                return half * half * a

        if n < 0:
            return fpow(1 / x, -n)
        else:
            return fpow(x, n)