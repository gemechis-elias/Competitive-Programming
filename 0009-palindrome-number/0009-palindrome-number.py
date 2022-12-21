class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = 0
        r = len(x)-1
        while l <= r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
