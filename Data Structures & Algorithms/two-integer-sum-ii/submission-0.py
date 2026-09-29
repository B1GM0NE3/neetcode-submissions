class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_p, right_p = 0, len(numbers) - 1
        while left_p < right_p:
            if numbers[left_p] + numbers[right_p] == target:
                return [left_p + 1, right_p + 1]
            if numbers[left_p] + numbers[right_p] > target:
                right_p -= 1
            else:
                left_p += 1
        return []