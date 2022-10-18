class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count={0:1}
        count_subarray=0
        tempsum=0
        for i in nums:
            tempsum+=i
            temp=tempsum-k
            if temp in prefix_count: count_subarray+=prefix_count[temp]
                
            if tempsum in prefix_count: prefix_count[tempsum ]+=1
                
            else: prefix_count[tempsum]=1

            
        return count_subarray
