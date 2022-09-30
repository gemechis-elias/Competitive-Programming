def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    count=[0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and  nums[i]>nums[j]:
                count[i]+=1
    return count
