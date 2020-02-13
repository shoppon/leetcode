#coding: utf-8
import sys
sys.setrecursionlimit(10000)


class Solution:

    def superEggDrop1(self, K: int, N: int) -> int:

        mem = {}

        def dp(k, n):
            # 如果只有一层楼则只需要1次
            if n == 0:
                return 0
            # 如果只有一个鸡蛋则需要n次
            if k == 1:
                return n
            if (k, n) in mem:
                return mem[(k, n)]

            min_v = float('inf')
            left = 1
            right = n
            while left <= right:
                mid = (left + right) // 2
                # 在i层楼扔鸡蛋分为碎与不碎两种情况
                # 碎了则在k-1个鸡蛋在0~i-1层楼中检查
                # 不碎则k个鸡蛋在i+1~n层楼中检查
                left_v = dp(k-1, mid-1)
                right_v = dp(k, n-mid)
                if left_v < right_v:
                    left = mid + 1
                    min_v = min(min_v, right_v+1)
                else:
                    right = mid - 1
                    min_v = min(min_v, left_v+1)

            mem[(k, n)] = min_v
            return min_v

        ans = dp(K, N)
        return ans

    def superEggDrop(self, K: int, N: int) -> int:

        mem = {}

        def dp(k, n):
            # 如果只有一层楼则只需要1次
            if n == 0:
                return 0
            # 如果只有一个鸡蛋则需要n次
            if k == 1:
                return n
            if (k, n) in mem:
                return mem[(k, n)]

            left, right = 1, n
            while left + 1 < right:
                mid = (left + right) // 2
                # 在i层楼扔鸡蛋分为碎与不碎两种情况
                # 碎了则在k-1个鸡蛋在0~i-1层楼中检查
                # 不碎则k个鸡蛋在i+1~n层楼中检查
                left_v = dp(k-1, mid-1)
                right_v = dp(k, n-mid)
                if left_v < right_v:
                    left = mid + 1
                elif left_v > right_v:
                    right = mid - 1
                else:
                    left = right = mid

            min_v = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                            for x in (left, right))
            mem[(k, n)] = min_v
            return min_v

        ans = dp(K, N)
        return ans
