# "5#hello5#world"
#  i = 0, j = 1
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s = s + f"{len(strs[i])}#{strs[i]}"
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start_index = j + 1
            res.append(s[start_index:start_index+length])
            i = start_index+length
        return res
