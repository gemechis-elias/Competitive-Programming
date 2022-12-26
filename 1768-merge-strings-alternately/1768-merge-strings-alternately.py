class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        ans = ""
        for i in range(n):
            ans += word1[i]
            ans += word2[i]
        if len(word1) > n:
            tmp = word1[n:len(word1)]
            ans += tmp
        if len(word2) > n:
            tmp = word2[n:len(word2)]
            ans += tmp
        return ans
        