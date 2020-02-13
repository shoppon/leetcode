from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        even = total % 2 == 0
        count = (total) // 2 + 1

        while count:
            m = nums1[0] if nums1 else float('inf')
            n = nums2[0] if nums2 else float('inf')
            if m <= n:
                nums1.pop(0)
                ret = m
            else:
                nums2.pop(0)
                ret = n
            if count == 2 and even:
                pre = ret
            count -= 1
        if even:
            return (pre + ret) / 2
        else:
            return ret
