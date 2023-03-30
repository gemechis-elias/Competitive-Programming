class Solution:
    def findComplement(self, num: int) -> int:
        str_bit = bin(num)
        bit_ = list(str_bit)
        
        for i in range(2, len(bit_)):
            if bit_[i] == "1":
                bit_[i] = "0"
            else:
                bit_[i] = "1"
        
        ans = ""
        for i in bit_[2:]:
            ans += i
        


        return int(ans, 2)