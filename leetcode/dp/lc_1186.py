from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        arr_len = len(arr)
        if arr_len == 1:
            return arr[0]

        has_del = [0] * arr_len
        no_del = [0] * arr_len

        no_del[0] = arr[0]
        for i in range(1, arr_len):
            # 未删除时最大值为当前值和累加值的较大值
            no_del[i] = max(arr[i], no_del[i-1]+arr[i])

        has_del[0] = arr[0]
        has_del[1] = max(arr[0], arr[1])
        for i in range(2, arr_len):
            # 删除一次要么删除自己，要么删除的时其他
            has_del[i] = max(no_del[i-1], has_del[i-1]+arr[i])

        return max(has_del + no_del)
