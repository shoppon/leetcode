from typing import List


class Solution:
    def nextGreaterElements1(self, nums: List[int]) -> List[int]:
        ans = []
        count = len(nums)
        for i, n in enumerate(nums):
            cur = i
            for _ in range(count):
                cur += 1
                if nums[cur % count] > n:
                    ans.append(nums[cur % count])
                    break
            else:
                ans.append(-1)
        return ans

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈里记录坐标
        stack = []
        l = len(nums)
        ans = [-1] * l
        for i in range(2*l - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % l]:
                stack.pop()
            # 栈顶元素即是比当前大的下一个元素
            ans[i % l] = -1 if stack == [] else nums[stack[-1]]
            stack.append(i % l)
        return ans
