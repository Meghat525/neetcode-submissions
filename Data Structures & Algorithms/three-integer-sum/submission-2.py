# [ 3, -6, 0, -3, 2, 4 ] : [[3, 0, -3], [-6, 2 , 4]]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # If the smallest number is > 0, it is impossibile for the sum to be 0
            if nums[i] > 0:
                break
            # To skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if target - nums[l] > nums[r]:
                    l += 1
                elif target - nums[l] < nums[r]:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    # Skip duplicates for the left pointer to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
