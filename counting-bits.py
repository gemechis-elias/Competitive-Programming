class Solution:
    def countBits(self, n: int) -> List[int]:
   
        new_ = [0]*(n+1)
        if n > 0:
            new_[1] = 1

        for i in range(n+1):
            if i % 2 == 0:
                new_[i] = new_[i//2]
            else:
                new_[i] = new_[i//2]+1
        return new_