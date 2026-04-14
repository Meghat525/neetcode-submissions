# nums = (100,4,200,1,3,2, 200, 201)
# {200:201, 1:2, 3: 4, 2:3}
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums = set(nums)
        max_len = curr_len = 0
        for i in nums:
            if i-1 not in nums:
                curr_len = 1
                while i + curr_len in nums:
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len

