class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        idx=len(arr)
       
        while idx > 0:
            
            flips = max(arr[:idx])
            flips = arr.index(flips)
            
            if flips !=0:
                res.append(flips + 1)
               
            arr[:flips +1]= reversed(arr[:flips +1])
            arr[:idx] = reversed(arr[:idx])
            
            res.append(idx)
            idx-=1
            
        return res
