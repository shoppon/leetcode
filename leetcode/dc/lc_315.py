from typing import List


class Solution:
    def countSmaller1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        mins = []
        maxs = []
        min_v = float('inf')
        max_v = float('-inf')
        for i in range(n-1, -1, -1):
            min_v = min(min_v, nums[i])
            max_v = max(max_v, nums[i])
            mins.insert(0, min_v)
            maxs.insert(0, max_v)

        for i in range(n):
            count = 0
            for j in range(i+1, n):
                # 比最小的还小，肯定没有比他更小的了
                if nums[i] < mins[j]:
                    break
                # 比最大的还大，那没必须再遍历了
                if nums[i] > maxs[j]:
                    count += (n-j)
                    break
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans

    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        tmp = [None] * size
        indexes = [i for i in range(size)]
        ans = [0] * size

        self.merge_sort(nums, 0, size - 1, tmp, indexes, ans)
        return ans

    def merge_sort(self, nums, left, right, tmp, indexes, ans):
        if left == right:
            return

        mid = left + (right - left) // 2
        self.merge_sort(nums, left, mid, tmp, indexes, ans)
        self.merge_sort(nums, mid + 1, right, tmp, indexes, ans)

        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        self.merge(nums, left, mid, right, tmp, indexes, ans)

    def merge(self, nums, left, mid, right, tmp, indexes, ans):
        for i in range(left, right + 1):
            tmp[i] = indexes[i]

        l = left
        r = mid + 1
        for i in range(left, right + 1):
            if l > mid:
                indexes[i] = tmp[r]
                r += 1
            elif r > right:
                indexes[i] = tmp[l]
                l += 1
                ans[indexes[i]] += (right - mid)
            elif nums[tmp[l]] <= nums[tmp[r]]:
                indexes[i] = tmp[l]
                l += 1
                ans[indexes[i]] += (r - mid - 1)
            else:
                indexes[i] = tmp[r]
                r += 1
