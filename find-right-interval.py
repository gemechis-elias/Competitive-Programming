class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        
        ans = [-1]*len(ints)
        
        begins = [i for i,j,k in ints]
        
        for i,j,k in ints:
            t = bisect_left(begins,j)
            if t < len(ints):
                ans[k] = ints[t][2]
        
        return ans