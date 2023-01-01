left = 0
  for i in range(len(nums)):
      if nums[i] !=0:
          nums[left], nums[i] = nums[i], nums[left]
          left += 1
