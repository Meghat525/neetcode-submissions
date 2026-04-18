class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_length = 0
        result = None
        hashmap = {}
        for j in range(len(s)):
            hashmap[s[j]] = hashmap.get(s[j], 0) + 1
            max_f = max(hashmap.values())
            if j - i + 1 - max_f > k:  
                hashmap[s[i]] = hashmap.get(s[i], 1) - 1
                i += 1

            if j - i + 1 > max_length:
                max_length = j - i + 1

        return max_length