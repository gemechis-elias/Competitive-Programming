class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        for i in range(max(x,y).bit_length()):
            if x & (1<<i) != y & (1<<i):
                d += 1

        return d