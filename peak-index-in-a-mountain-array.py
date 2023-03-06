class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)-1
        mid = s + (n-s) // 2
        while s < n:
            if arr[mid] < arr[mid+1]:
                s = mid + 1
            else:
                n = mid
            mid = s + (n-s)//2
        return s