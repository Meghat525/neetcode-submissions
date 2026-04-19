class Solution:
    def is_matching(self, hashmap: dict, new_map: dict) -> bool:
        for key in hashmap:
            if hashmap[key] > new_map.get(key, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        hashmap = {}
        for i in t:
            hashmap[i] = hashmap.get(i, 0) + 1
        new_map = {}
        have = 1
        need = len(hashmap)
        min_len = float("infinity")
        res = []
        l = r = 0
        while r < len(s):
            if s[r] in hashmap:
                new_map[s[r]] = new_map.get(s[r], 0) + 1
            while self.is_matching(hashmap, new_map):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = [l, r]

                if s[l] in new_map:
                    new_map[s[l]] = new_map.get(s[l], 0) - 1
                    if new_map.get(s[l], 0) < 1:
                        new_map.pop(s[l])
                l += 1
            r += 1
        if res == []:
            return ""
        else:
            return s[res[0] : res[1] + 1]      