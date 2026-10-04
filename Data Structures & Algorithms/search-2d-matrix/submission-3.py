class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, gap = 0, len(matrix[0])
        r = gap * (len(matrix) - 1) + len(matrix[-1]) - 1
        while l <= r:
            m = l + (r - l) // 2
            guess = matrix[m // gap][m % gap]

            if guess == target:
                return True
            elif guess < target:
                l = m + 1
            else:
                r = m - 1
        return False
