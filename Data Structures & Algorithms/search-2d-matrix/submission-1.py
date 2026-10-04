class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                l, r = 0, len(matrix[i]) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    guess = matrix[i][m]

                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
        return False
