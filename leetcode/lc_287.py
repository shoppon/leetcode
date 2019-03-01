class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        for i in range(1, nums_len + 2):
            exist = 0
            for n in nums:
                if i == n:
                    if exist == 1:
                        return i
                    else:
                        exist = 1
