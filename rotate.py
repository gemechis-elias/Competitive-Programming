class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        if k != 0: 
            last = nums[-k:] 
            for i in range(n-k-1, -1, -1): 
                nums[i+k] = nums[i]  
            nums[:k] = last  
