class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = [list(i) for i in strs]
        result = 0
        z = zip(*(ans))
        for i in z:
            if list(i)!=sorted(i):
                result+=1
        
        return result
