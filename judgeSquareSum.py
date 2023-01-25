class Solution(object):
    def judgeSquareSum(self, c):
        rootC = int(c ** 0.5)
        low, high = 0, rootC
        while low <= high:
            result = low ** 2 + high ** 2
            print(low ** 2, high ** 2)
            if result == c:
                return True
            elif result > c:
                high -= 1
            else:
                low += 1
                
        return False
