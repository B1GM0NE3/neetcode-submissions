class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        zeros, product, res = 0, 1, []
        for i in nums:
            if i == 0:
                zeros += 1
                continue
            product *= i

        if zeros > 1:
            res = [0]*len(nums)
        elif zeros == 1:
            for i in nums:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
        else:
            for i in nums:
                res.append(product // i)
        return res