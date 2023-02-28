class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return 0
        if n ==1:
            return 1
        n = n/3
        return self.isPowerOfThree(n)
