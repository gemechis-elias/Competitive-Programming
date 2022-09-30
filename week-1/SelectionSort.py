def selectionSort(self, arr,n):
     for i in range(n):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min__index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
