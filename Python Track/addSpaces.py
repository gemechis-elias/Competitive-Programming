class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        idx = 0
        temp = ""
        for sp in spaces:
            ans.append(s[idx:sp]+" ")
            n = sp-idx
            idx += n
        ans.append(s[idx:])
        for i in ans:
            temp += i
        return temp
