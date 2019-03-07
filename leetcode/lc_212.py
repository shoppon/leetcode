class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        x_len = len(board)
        y_len = len(board[0])
        for word in words:
            for w in word:
                for i in range(x_len):
                    j = 0
                    if w != board[i][j]:
                        continue
                    for j in range(y_len):
                        if w != board[i][j]:
                            continue
