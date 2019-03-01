class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for n in nums:
            if n > 0 and n not in nums_dict:
                nums_dict[n] = 1
        for i in range(1, len(nums) + 2):
            if i not in nums_dict:
                return i
