class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        total_product_when_0 = 1
        count_0 = 0
        for i in range(len(nums)):
            total_product = total_product * nums[i]
            if nums[i] == 0 and count_0 == 0:
                count_0 += 1
            else:
                total_product_when_0 = total_product_when_0 * nums[i]
        prod_list = []
        if count_0 > 1:
            return [0] * len(nums)
        elif count_0 == 1:
            for element in nums:
                if element == 0:
                    prod_list.append(total_product_when_0)
                else:
                    prod_list.append(0)
        else:
            for element in nums:
                prod_list.append(int(total_product/element))
        return prod_list
