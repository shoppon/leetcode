from typing import List


class Solution:
    def diffWaysToCompute(self, arr: str) -> List[int]:
        if arr.isdigit():
            return [int(arr)]

        ans = []

        for i, char in enumerate(arr):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(arr[:i])
                right = self.diffWaysToCompute(arr[i+1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            ans.append(l+r)
                        elif char == '-':
                            ans.append(l-r)
                        else:
                            ans.append(l*r)

        return ans
