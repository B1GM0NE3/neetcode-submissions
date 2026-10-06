class Solution:
    def climbStairs(self, n: int) -> int:
        stair_2 = 1
        stair_1 = 1
        for _ in range(n-1):
            mid = stair_1
            stair_1 = stair_1 + stair_2
            stair_2 = mid
        return stair_1
