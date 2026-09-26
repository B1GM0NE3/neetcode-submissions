class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
        
        grouped_cnt = [[] for i in range(len(nums) + 1)]
        for num, i in cnt.items():
            grouped_cnt[i].append(num)

        res = []
        for i in range(len(grouped_cnt)-1, 0, -1):
            for j in grouped_cnt[i]:
                res.append(j)
                if len(res) == k:
                    return res