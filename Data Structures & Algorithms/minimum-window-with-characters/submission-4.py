class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        hashmap = {}
        for i in t:
            hashmap[i] = hashmap.get(i, 0) + 1
        new_map = {}
        min_len = float("infinity")
        res = []
        l = r = 0
        have = 0
        need = len(hashmap)
        while r < len(s):
            if s[r] in hashmap:
                new_map[s[r]] = new_map.get(s[r], 0) + 1
            if s[r] in hashmap and new_map[s[r]] == hashmap[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                if s[l] in hashmap:
                    new_map[s[l]] -= 1
                    if new_map[s[l]] < hashmap[s[l]]:
                        have -= 1
                l += 1
            r += 1
        if res == []:
            return ""
        else:
            return s[res[0] : res[1] + 1]      