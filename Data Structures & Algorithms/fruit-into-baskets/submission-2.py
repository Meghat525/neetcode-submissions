# [1,0,1,4,1,4,1,2,3]
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        l = r = 0
        hashmap = {}
        while r < len(fruits):
            hashmap[fruits[r]] = hashmap.get(fruits[r], 0) + 1
            while len(hashmap) > 2:
                left_fruit = fruits[l]
                hashmap[left_fruit] -= 1
                if hashmap[left_fruit] == 0:
                    del hashmap[left_fruit]
                l += 1
            
            max_len = max(r - l + 1, max_len)
            print(r - l + 1, max_len, l, r)
            r += 1
            
        return max_len
