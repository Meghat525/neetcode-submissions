class Solution:
    def subarrayWithLessThanEqualtoK(self, nums, k):
        l = r = 0
        hashmap = {}
        count = 0
        while r < len(nums):
            hashmap[nums[r]] = hashmap.get(nums[r], 0) + 1
            while len(hashmap) > k:
                hashmap[nums[l]] = hashmap[nums[l]] - 1
                if hashmap[nums[l]] == 0:
                    del hashmap[nums[l]]
                l += 1
            count += r - l + 1
            r += 1
        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrayWithLessThanEqualtoK(nums, k) - self.subarrayWithLessThanEqualtoK(nums, k-1)
        