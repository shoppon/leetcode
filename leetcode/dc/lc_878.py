from fractions import gcd


class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        L = A * B / gcd(A, B)
        low = 0
        high = 10**15

        def nums(A, B, L, x):
            return x // A + x // B - x // L

        while low < high:
            mid = (low + high) // 2
            if nums(A, B, L, mid) < N:
                low = mid + 1
            else:
                high = mid

        return low % (10**9 +7)
