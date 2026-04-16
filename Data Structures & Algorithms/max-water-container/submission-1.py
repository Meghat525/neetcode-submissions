class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        curr_water = 0
        # water will be min(height1, height2) * (index2 - index 1)
        l = 0
        r = len(height) - 1
        while l < r:
            curr_water = min(height[l], height[r]) * (r - l)
            max_water = max(curr_water, max_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water
