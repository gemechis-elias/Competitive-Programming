class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer = 0
        right_pointer = 1
        # use two pointers to swap
        while right_pointer < len(nums):
            # left_pointer value is always zero
            if nums[left_pointer] != 0:
                left_pointer += 1
                right_pointer += 1
                continue
            # right_pointer value is always non-zero
            if nums[right_pointer] == 0:
                right_pointer += 1
                continue
            
            # swap non-zero and zero values
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer += 1