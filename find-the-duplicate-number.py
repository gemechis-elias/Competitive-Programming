class Solution(object):
    def findDuplicate(self, nums):
        beg, end = 1, len(nums)-1
        
        while beg + 1 <= end:
            mid, count = (beg + end)//2, 0
            for num in nums:
                if num <= mid: count += 1        
            if count <= mid:
                beg = mid + 1
            else:
                end = mid
        return end