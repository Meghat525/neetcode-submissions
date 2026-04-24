class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashset = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in hashset.values():
                stack.append(c)
            elif c in hashset.keys():
                if not stack or hashset[c] != stack.pop():
                    return False
        
        return not stack