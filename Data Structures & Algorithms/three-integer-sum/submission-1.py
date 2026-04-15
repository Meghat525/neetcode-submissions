# [ 3, -6, 0, -3, 2, 4 ] : [[3, 0, -3], [-6, 2 , 4]]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_set = set()
        res = set()
        for i in range(len(nums) - 2):
            nums_set = set()
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                if target - nums[j] in nums_set:
                    res.add((nums[i], nums[j], target - nums[j]))
                nums_set.add(nums[j])
        res = list(res)
        return res

        