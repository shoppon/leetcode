from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traverse(arr):
            if len(arr) <= 1:
                return [arr]
            elif len(arr) == 2:
                return [arr, [arr[1], arr[0]]]
            else:
                ret = []
                for i, n in enumerate(arr):
                    tmp = traverse(arr[:i] + arr[i+1:])
                    for t in tmp:
                        ret.append([n] + t)
                return ret

        return traverse(nums)

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
                # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
