class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_1 = 0
        l = r = 0
        window = 0

        while r < len(nums):
            if nums[r] == 1:
                count_1 += 1
            if r - l + 1 - count_1 > k:
                if nums[l] == 1:
                    count_1 -= 1
                l += 1
            window = max(window, r - l + 1)
            r += 1
        
        return window
