class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left_max = height[0]
        right_max = height[-1]
        l = 0
        r = len(height) - 1
        while l < r:
            if left_max > right_max:
                r -= 1
                total_water += max(0, min(left_max, right_max) - height[r])
            else:
                l += 1
                total_water += max(0, min(left_max, right_max) - height[l])
            if height[l] > left_max:
                left_max = height[l]
            elif height[r] > right_max:
                right_max = height[r]
        return total_water