class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans=[]
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for distance in range(1,8):
                    x = king[0] + i*distance
                    y = king[1] + j*distance
                    
                    if [x,y] in queens:
                        ans.append([x,y])
                        break
        return ans
