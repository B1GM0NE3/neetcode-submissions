class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for i in nums:
            cnt[i] = 1 + cnt.get(i, 0)
        
        sorted_cnt = []
        for num, cnt in cnt.items():
            sorted_cnt.append([cnt, num])
        sorted_cnt.sort()

        res = []
        for _ in range(k):
            res.append(sorted_cnt.pop()[1])
        return res
        