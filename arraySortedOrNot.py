class Solution:
    def arraySortedOrNot(self, arr, n):
        i = 0
        j = i+1
        while i < n-1:
            if arr[i]>arr[j]:
                return False
            i+=1
            j+=1
        return True
        
