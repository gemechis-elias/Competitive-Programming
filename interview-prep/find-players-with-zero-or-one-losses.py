from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dct=defaultdict(lambda :[0,0])
        for p1,p2 in matches:
            dct[p1][0]+=1
            dct[p1][1]+=1
            dct[p2][0]+=1
        wonAll=[]
        lossOne=[]
        for i in dct:
            if dct[i][0]==dct[i][1]:
                wonAll.append(i)
            elif dct[i][0]-dct[i][1]==1:
                lossOne.append(i)
        wonAll.sort()
        lossOne.sort()
        return [wonAll,lossOne]