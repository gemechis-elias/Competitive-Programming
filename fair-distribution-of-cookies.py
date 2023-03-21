class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = [0]*k
        self.res = float("inf")
        def backtrack(curr):
            if curr==len(cookies):
                # print(n)
                self.res=min(self.res,max(n))
                return
            if max(n)>=self.res:
                return
            for i in range(k):
                n[i]+=cookies[curr]
                backtrack(curr+1)
                n[i]-=cookies[curr]
                if n[i] == 0:
                    break
        backtrack(0)
        return self.res