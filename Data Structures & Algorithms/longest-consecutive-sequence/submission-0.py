# nums = (100,4,200,1,3,2, 200, 201)
# {200:201, 1:2, 3: 4, 2:3}
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums = set(nums)
        next_element_dict = {}
        for i in nums:
            if i + 1 in nums:
                next_element_dict[i] = i + 1
        if len(next_element_dict) == 0:
            return 1
        c = 0
        curr_len = max_len = 2
        l_keys = list(set(next_element_dict.keys()))
        length_dict = {}
        seen = set()
        key = l_keys[0]
        while c < len(next_element_dict):
            if key in seen and c != len(next_element_dict) - 1:
                c += 1
                key = l_keys[c]
                continue
            elif (key - 1 not in next_element_dict or key -1 in seen) and next_element_dict[key] in next_element_dict:
                curr_len += 1
                max_len = max(curr_len, max_len)
                seen.add(key)
                key = next_element_dict[key]
            else:
                c += 1
                if c != len(next_element_dict):
                    key = l_keys[c]
                curr_len = 2
        return max_len

