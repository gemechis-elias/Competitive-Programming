class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize left and right pointers, oddCount and count variables
        left = 0
        right = 0
        oddCount = 0
        count = 0
        
        # Iterate through the array using right pointer
        while right < len(nums):
            # If current number is odd, increment oddCount
            if nums[right] % 2 != 0:
                oddCount += 1
                
            # If oddCount is equal to k, calculate the number of subarrays that can be formed from current window
            if oddCount == k:
                # Count the number of subarrays that can be formed by extending the window to the right
                subarrays = 1
                while right+1 < len(nums) and nums[right+1] % 2 == 0:
                    subarrays += 1
                    right += 1
                    
                # Count the number of subarrays that can be formed by extending the window to the left
                leftSubarrays = 1
                while nums[left] % 2 == 0:
                    leftSubarrays += 1
                    left += 1
                    
                # Update the count variable by multiplying the counts from both sides
                count += subarrays * leftSubarrays
                
                # Move the left pointer to the next odd number and decrement oddCount
                left += 1
                oddCount -= 1
            
            # Increment right pointer
            right += 1
            
        # Return the count variable
        return count
