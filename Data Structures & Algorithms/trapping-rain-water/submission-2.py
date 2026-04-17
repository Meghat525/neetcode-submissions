class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left_max_l = [0] * len(height)
        right_max_l = [0] * len(height)
        left_max = 0
        right_max = 0
        for i in range(1, len(height)):
            if height[i - 1] > left_max:
                left_max = height[i - 1]
            left_max_l[i] = left_max

        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > right_max:
                right_max = height[i + 1]
            right_max_l[i] = right_max
        for i in range(len(height)):
            total_water += max(0, min(left_max_l[i], right_max_l[i]) - height[i])

        return total_water
