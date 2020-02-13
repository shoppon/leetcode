# coding: utf-8
class Solution(object):
    def simplifyPath(self, path):
        """

        用栈保存路径，如果是两个点并且则pop
        :type path: str
        :rtype: str
        """
        paths = []
        path_len = len(path)
        last = None
        for idx in range(path_len - 1, 0, -1):
            temp = path[idx]
            if temp == '.':
                if last == '.':
                    pass
            elif temp == '/':
                if last == '':
                    pass
            else:
                pass
