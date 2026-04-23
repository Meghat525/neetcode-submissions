class Solution:
    def numSubarrayswithLessThanSum(self, nums, goal):
        l = r = 0
        count = 0
        total = 0
        if goal < 0:
            return 0
        while r < len(nums):
            total += nums[r]
            while total > goal:
                total -= nums[l]
                l += 1
            count += r - l + 1
            r += 1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.numSubarrayswithLessThanSum(nums, goal) - self.numSubarrayswithLessThanSum(nums, goal - 1)
        