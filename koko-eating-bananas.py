class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left <= right:
            mid =  (left + right)//2
            hour = 0
            for b in piles:
                hour += ceil(b/mid)

            if hour > h:
                left = mid +1
            else:
                right = mid -1


        return left