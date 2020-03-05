import math


class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if n > 0:
            ans = 1
            while n:
                ans *= x
                n -= 1
        elif n < 0:
            ans = 1
            while -n:
                ans *= x
                n += 1
            ans = 1/ans
        else:
            ans = 1

        return ans

    def myPow(self, x, n)
        return math.pow(x, n)
