class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #? [9,8,7,6,5,1,2,3,4] 
        # [2,4,1,2,7,8] -> 1,2,2,4,7,8.  8,7,1
        sum_ = 0
        res = []
        piles.sort()
        for i in range(len(piles)):
            temp = []
            end = len(piles)
            if i < end-1:
                temp.append(piles[i])
                temp.append(piles[-1])
                temp.append(piles[-2])
                piles.pop()
                piles.pop()
            else:
                break
            res.append(temp)
        for j in res:
            j.sort()
            sum_ += j[1]
            print(j)
        return sum_
