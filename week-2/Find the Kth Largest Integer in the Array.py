class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def order(x):
            y=int(x)
            return y
        n=len(nums)
        nums.sort(key=order)
        answer=nums[n-k]
        return answer
