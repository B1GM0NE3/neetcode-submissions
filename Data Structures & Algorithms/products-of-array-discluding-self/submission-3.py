class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        lengh, zeros, product, res = 0, 0, 1, []
        for i in nums:
            if i == 0:
                zeros += 1
                lengh += 1
                continue
            product *= i
            lengh += 1

        if zeros > 1:
            res = [0]*lengh
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