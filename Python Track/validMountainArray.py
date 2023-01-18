class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        mountain_array = False
        bottom_to_top =0
        top_to_bottom =0
        head = max(arr)
        i, j = arr.index(head), arr.index(head)
        if i != 0 and i != len(arr)-1:
            while i < len(arr)-1:
                if arr[i] > arr[i+1]:
                    top_to_bottom += 1
                i += 1
            while j > 0:
                if arr[j] > arr[j-1]:
                    bottom_to_top += 1
                j -= 1
        if bottom_to_top + top_to_bottom == len(arr)-1:
            return not mountain_array
                
            
            
