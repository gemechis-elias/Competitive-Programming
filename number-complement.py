class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = num.bit_length()
        #print(num_bits)
        complement = ~num & ((1 << num_bits) - 1)

        return complement