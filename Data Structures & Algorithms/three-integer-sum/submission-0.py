# [ 3, -6, 0, -3, 2, 4 ] : [[3, 0, -3], [-6, 2 , 4]]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_set = set()
        res = []
        for i in range(len(nums) - 2):
            nums_set = set()
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                if target - nums[j] in nums_set:
                    res.append(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                nums_set.add(nums[j])
        res = list(set(res))
        return res

        