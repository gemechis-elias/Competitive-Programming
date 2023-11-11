class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        start = defaultdict(lambda : -1)

        mx_count = 0
        for i in range(len(nums)):
            count[nums[i]]+=1
            mx_count = max(mx_count, count[nums[i]])

            if start[nums[i]] == -1:
                start[nums[i]] = i

        ans = len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            if count[nums[i]] == mx_count:
                ans = min(ans, i - start[nums[i]]+1)
                count[nums[i]]-=1

        
        
        return ans
                



        