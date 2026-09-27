class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        lengh, zeros, product, res = 0, 0, 1, []
        for i in nums:
            lengh += 1
            if i == 0:
                zeros += 1
                continue
            product *= i

        if zeros > 1:
            return [0]*lengh

        for i in nums:
            if zeros:
                if i == 0:
                    res.append(product)
                else: 
                    res.append(0)
            else:
                res.append(product // i)
        return res