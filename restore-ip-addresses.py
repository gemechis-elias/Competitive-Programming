class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, curr):
            if len(curr) == 4 and start == len(s):
                res.append(".".join(curr))
            elif len(curr) == 4 or start == len(s):
                return
            for i in range(1, 4):
                if start + i <= len(s) and (s[start] != "0" or i == 1) and int(s[start:start+i]) <= 255:
                    curr.append(s[start:start+i])
                    backtrack(start+i, curr)
                    curr.pop()
                    
        res = []
        backtrack(0, [])
        return res