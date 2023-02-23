class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left =0
        right =  0
        ans = 0
        n = len(arr)
        if n == 1:
            return 1
        while right < n:
            while right < n-1 and (arr[right-1]>arr[right]<arr[right+1] or arr[right-1]<arr[right]>arr[right+1]):
                right+=1
            while left < right and arr[left]==arr[left+1]:
                left+=1
            ans = max(ans,right-left+1)
            left = right
            right+=1

        return ans
