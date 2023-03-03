# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n
        l = 0
        bad_version = 0

        while l <= r:
            mid = (r + l)//2
            if isBadVersion(mid):
                bad_version = mid
                r = mid - 1 
            else:
                l = mid + 1

        return bad_version