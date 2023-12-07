class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        cur = s[:10]
        count = Counter()
        count[cur] = 1
        for i in range(1, len(s) - 9):
            cur = cur[1:] + s[i + 9]
            count[cur] += 1
        ans = []
        for key in count:
            if count[key] > 1:
                ans.append(key)
        return ans
        



        