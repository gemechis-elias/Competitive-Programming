class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        result=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid > x:
                right=mid-1
            elif mid*mid < x:
                left=mid+1
                result = max(result,mid)
            else:
                return mid
        return result