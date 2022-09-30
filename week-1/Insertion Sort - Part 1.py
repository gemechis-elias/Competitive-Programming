def insertionSort1(n, arr):
    pos=n-1
    cur_value=arr[pos]
    while curt_value<arr[pos-1] and pos>0:
        arr[pos]=arr[pos-1]
        pos-=1
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
    arr[pos]=cur_value
    for i in range(len(arr)):
            print(arr[i],end=" ")
