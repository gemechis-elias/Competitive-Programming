class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * n
        
        for l, r in requests:
            freq[l] += 1
            if r < n - 1:
                freq[r + 1] -= 1
                
        for i in range(1, n):
            freq[i] += freq[i - 1]
                
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        ans = 0
        for i in range(n):
            ans += nums[i] * freq[i]
        print(ans % (10**9 + 7))   
        return ans % (10**9 + 7)
