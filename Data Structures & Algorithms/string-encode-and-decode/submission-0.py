import base64
class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = base64.b64encode("#".encode('utf-8'))
        delimiter = delimiter.decode('utf-8')
        s = ""
        for i in range(len(strs)):
            s = s + str(len(strs[i])) + delimiter
        for i in range(len(strs)):
            s = s + strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        delimiter = base64.b64encode("#".encode('utf-8'))
        delimiter = delimiter.decode('utf-8')
        strs_1 = []
        # print(len(delimiter))
        length = []
        strs_1 = s.split(delimiter)
        strs = []
        s = strs_1[-1]
        strs_1.pop(-1)
        for i in range(len(strs_1)):
            strs.append(s[:int(strs_1[i])])
            s = s[int(strs_1[i]):]
        return strs
