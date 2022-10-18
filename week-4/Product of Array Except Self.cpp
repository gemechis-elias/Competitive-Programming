class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n
        prefixmul=1
        postfixmul=1
        index=n-1
        for i in range(1,n):
            prefixmul*=nums[i-1]
            output[i]=prefixmul
            
        for i in range(n-2,-1,-1):
            postfixmul*=nums[i+1]
            output[i]*=postfixmul
        return output
