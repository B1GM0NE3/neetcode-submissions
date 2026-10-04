class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            index = (r + l) // 2
            guess = nums[index]

            if guess == target:
                return index
            elif guess < target:
                l = index + 1
            else:
                r = index - 1
        return -1
            

