class Solution:
    def binary_search(self, l, r, nums, target):
        if l > r:
            return -1

        index = (l + r) // 2
        guess = nums[index]
        if guess == target:
            return index
        elif guess < target:
            return self.binary_search(index + 1, r, nums, target)
        return self.binary_search(l, index - 1, nums, target)
        
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
            

