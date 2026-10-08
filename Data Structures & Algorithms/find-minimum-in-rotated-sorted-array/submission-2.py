class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        for i in range(len(nums)):
            if nums[i] < nums[i-1]: 
                mini = min(mini, nums[i])
                break
        return mini

                        
