class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        hashmap = {1: 0, 0: 0}
        l = r = 0
        window = 0
        while r < len(nums):
            hashmap[nums[r]] += 1
            if r - l + 1 - hashmap[1] > k:
                hashmap[nums[l]] -= 1
                l += 1
            window = max(window, r - l + 1)
            r += 1
        
        return window
        