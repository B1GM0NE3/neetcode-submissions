class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, vol = 0, len(heights) - 1, 0
        while l < r:
            temp = (r - l) * min(heights[l], heights[r])
            vol = max(vol, temp)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return vol
