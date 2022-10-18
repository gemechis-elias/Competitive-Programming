class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0: nums[i]=0
            else: nums[i]=1

        prefix_count={0:1}
        count_subarray=0
        tempsum=0
        for i in nums:
            tempsum+=i
            temp=tempsum-k

            if tempsum in prefix_count: prefix_count[tempsum ]+=1
            else: prefix_count[tempsum]=1

            if temp in prefix_count: count_subarray+=prefix_count[temp]
        return count_subarray
