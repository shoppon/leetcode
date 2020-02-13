class Solution():
    def crackSafe1(self, n: int, k: int) -> str:
        pass

    def crackSafe(self, n, k):
        seen = set()
        ans = []

        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)

    def permutations(self, n, elems):
        def recursive(index):
            if index == n:
                print("".join(number))
                return
            for e in elems:
                number[index] = e
                recursive(index+1)

        number = ['']*n
        recursive(0)
