def selectionSort(self, arr,n):
     for i in range(n):
        min_value_index = i
        for j in range(i+1,len(arr)):
            if arr[min_value_index]>arr[j]:
                min_value_index=j
        arr[i],arr[min_value_index]=arr[min_value_index],arr[i]
