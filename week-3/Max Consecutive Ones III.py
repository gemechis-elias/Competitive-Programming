class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left = 0
        right= 0
        maxsize = 0
        zerocount = 0
        while right<n:
            if nums[right]==0:
                zerocount+=1
            while zerocount>k:
                if nums[left]==0: zerocount-=1
                left+=1
            maxsize=max(maxsize,right-left+1)
            right += 1     
        return maxsize
