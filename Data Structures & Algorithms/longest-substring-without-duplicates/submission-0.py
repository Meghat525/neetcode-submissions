class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        r = 1
        max_len = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        hashset.add(s[l])
        while r < len(s):
            if s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            else:
                hashset.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
        return max_len