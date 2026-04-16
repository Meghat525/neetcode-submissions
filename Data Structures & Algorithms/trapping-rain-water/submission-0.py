class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        prev_min = 0
        l = 0
        r = len(height) - 1
        max_seen = max(height)
        all_heights = set(height)
        prev_min = 0
        water = 0
        while l < r:
            if height[l] > 0 and height[r] > 0:
                water += (min(height[l], height[r]) * (r - l - 1))
                prev_min = min(height[l], height[r])
                for i in range(l + 1 , r):
                    water -= min(height[l], height[r], height[i])
                    height[i] = max(0, height[i]-min(height[l], height[r]))
                if height[l] == height[r]:
                    height[l] = height[r] = 0
                elif height[l] < height[r]:
                    height[r] -= height[l]
                    height[l] = 0
                else:
                    height[l] -= height[r]
                    height[r] = 0
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water
        