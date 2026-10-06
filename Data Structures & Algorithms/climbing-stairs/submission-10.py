class Solution:
    def climbStairs(self, n: int) -> int:
        vault = {n+1: 0}
        def dfs(i):
            if i >= n:
                return i == n
            vault[i+1] = dfs(i+1)
            return vault[i+1] + vault[i+2]

        return dfs(0)
