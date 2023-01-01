# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    n = int(input())
    block = [int(x) for x in input().split()]
    left, right = 0, n-1
    if block[0] > block[-1]:
        top = block[0]
    else:
        top = block[-1]
    while left<right:
        if block[left]>= block[right]:
            if top >= block[left]:
                top = block[left]
                left +=1
            else:
                print("No")
                break
        else:
            if top >= block[right]:
                top = block[right]
                right -=1
            else:
                print("No")
                break
    if left == right:
        print("Yes")
        
    
