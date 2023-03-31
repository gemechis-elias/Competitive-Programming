class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit_val = list(bin(n)[2:])

        for i in range(1, len(bit_val)):
            if bit_val[i-1] == bit_val[i]:
                return 0
            
        return 1