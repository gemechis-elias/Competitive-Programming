class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = Counter(s1)
        
        window = {}
        k = len(s1)
        n = len(s2)
        left = 0
        for i in range(n):
            window[s2[i]] = window.get(s2[i], 0)+1
            if window == hashMap:
                return True
            if i-left+1== k:
                window[s2[left]] -= 1
                if window[s2[left]]==0:
                    window.pop(s2[left])
                left +=1
            print(window)
        return False
            
                
            
