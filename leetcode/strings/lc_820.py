from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = ""
        sorted_words = sorted(words, key=lambda x: -len(x))
        for w in sorted_words:
            if (w + "#") not in ans:
                ans += (w+'#')
        return len(ans)
