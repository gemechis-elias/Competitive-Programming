class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def finder(firstlen,secondlen):
            f_sum=s_sum=0
            limit=firstlen+secondlen
            for i in range(limit):
                if i<firstlen : f_sum+=nums[i]
                else : s_sum+=nums[i]
            
            maximum_L_M_sum=s_sum+f_sum
            f_max=f_sum
            for j in range(limit,len(nums)):
                s_sum+=nums[j]-nums[j-firstlen]
                f_sum+=nums[j-firstlen]-nums[j-firstlen-secondlen]
                f_max=max(f_max,f_sum)
                maximum_L_M_sum=max(maximum_L_M_sum,f_max+s_sum)
            
            return  maximum_L_M_sum
        result= max(finder(firstLen,secondLen), finder(secondLen,firstLen))
        return result
