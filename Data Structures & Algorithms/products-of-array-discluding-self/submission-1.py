class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        suffix_product = 1
        prod_list = [1] * len(nums)
        for i in range(1, len(nums)):
                prod_list[i] = nums[i - 1] * prod_list[i - 1]
        for i in range(len(nums) - 2, -1, -1):
                suffix_product = suffix_product * nums[i + 1]
                prod_list[i] = suffix_product * prod_list[i]
        return prod_list
