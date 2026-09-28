class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        res, count = 1, 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                if res < count:
                    res = count
                count = 1
        return max(res, count)