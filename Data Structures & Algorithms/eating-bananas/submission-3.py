class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2

            counth = 0
            for p in piles:
                counth += (p // k + 1 if p % k > 0 else p // k)   

            if counth <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            

            