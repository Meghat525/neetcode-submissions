class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if height[l] <= height[r]:
                if left_max > height[l]:
                    total_water += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if right_max > height[r]:
                    total_water += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1

        return total_water
