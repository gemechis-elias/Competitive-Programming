class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        strs.sort(key=len)
        for i in range(len(strs[0])):
            exist = True
            for j in strs:
                if j[i] != strs[0][i]:
                    exist = False
                    break
            if exist:
                ans += strs[0][i]
            else:
                return ans
        return ans
