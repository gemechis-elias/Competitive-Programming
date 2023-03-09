class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=1
        right=citations[-1]
        result=0

        while left<=right:
            mid=(left+right)//2
            curr = bisect_left(citations,mid)
          
            if len(citations)-curr>=mid:
                result = max(result,mid)
                left=mid+1
            else:
                right=mid-1

        return result