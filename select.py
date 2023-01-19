class Solution: 
    def select(self, arr, i):
         selectionSort(arr, i)
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min_ = i
            
            for element in range(i, len(arr)):
                if arr[element] < arr[min_]:
                    min_= element
                
            arr[i], arr[min_] = arr[min_], arr[i]
