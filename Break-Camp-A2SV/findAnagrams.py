class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]

        target = Counter(p)
            
        k = len(p)
        n = len(s)
        window = {}
        left = 0
        for i in range(n):
            window[s[i]] = window.get(s[i], 0)+1
            if target == window:
                ans.append(left)
                
            if i-left+1== k:
                window[s[left]] -= 1
                if window[s[left]]==0:
                    window.pop(s[left])
                left +=1
                
        return ans

