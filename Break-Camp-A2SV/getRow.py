class Solution:
    def getRow(self, n: int, ans=[1]) -> List[int]:
        temp = [1]
        if n == 0:
            return ans
            
        for i in range(1, len(ans)):
            temp.append(ans[i-1]+ans[i])
        temp.append(1)
        
        n -= 1
        return self.getRow(n, temp)  
           
