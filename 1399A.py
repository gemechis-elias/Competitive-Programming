n=int(input())
for _ in range(n):
    n=int(input())
    arr =list(map(int,input().split()))
    arr.sort()
 
    i = 0
    j = i + 1
    flag = True
    while flag and i < len(arr)-1:
        if arr[j] - arr[i] <= 1:
            arr.remove(arr[i])
            continue
        else:
            flag = True
      
        i +=1
        j +=1
    if len(arr)==1:
        print("YES")
    else:
        print("NO")
            
            
                
           

