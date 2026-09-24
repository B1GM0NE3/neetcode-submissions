class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, j in enumerate(nums):
            req = target - j
            if req in hash_map and hash_map[req] != i:
                return [hash_map[req], i]
            hash_map[j] = i
        return []
        
                
