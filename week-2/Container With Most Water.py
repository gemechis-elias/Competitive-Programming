class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        MostWater=0
        while left<right:
            heigh_t=min(height[right],height[left])
            cur=(right-left)*(heigh_t)
            MostWater=max(MostWater,cur)
            if height[right]>height[left]: left+=1
            else: right-=1
        return MostWater
