class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        product, res = 1, []
        for i in nums:
            if i == 0:
                continue
            product *= i
            
        if nums.count(0) > 1:
            return [0]*len(nums)
        elif nums.count(0) == 1:
            for i in nums:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res

        for i in nums:
            res.append(product // i)
        return res