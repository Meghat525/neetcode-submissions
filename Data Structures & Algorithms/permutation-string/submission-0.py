class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in s1:
            count1[ord(i) - ord('a')] += 1
        
        l = 0
        r = l + len(s1) - 1
        for i in range(l, r + 1):
            count2[ord(s2[i]) - ord('a')] += 1

        while r < len(s2):
            if count1 == count2:
                return True
            else:
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    count2[ord(s2[r]) - ord('a')] += 1

        return False