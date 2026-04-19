class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l + k - 1
        prev_max = max(nums[l: r + 1])
        res = [prev_max]
        while r < len(nums) - 1:
            if nums[r + 1] > prev_max:
                res.append(nums[r + 1])
                prev_max = nums[r + 1]
            elif prev_max == nums[l]:
                prev_max = max(nums[l + 1: r + 2])
                res.append(prev_max)
            else:
                res.append(prev_max)
            l += 1
            r += 1
        return res
        