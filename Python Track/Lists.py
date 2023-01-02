
ans = []
N = int(input())
for _ in range(N):
    my_input = input().split()
    if str(my_input[0]) == "insert":
        ans.insert(int(my_input[1]),int(my_input[2]))
    elif my_input[0] == "print":
        print(ans)
    elif my_input[0] == "remove":
        ans.remove(int(my_input[1]))
    elif my_input[0] == "sort":
        ans.sort()
    elif my_input[0] =="pop":
        ans.pop()
    elif my_input[0] == "reverse":
        ans = ans[::-1] 
    elif my_input[0] == "append":
        ans.append(int(my_input[1]))
        
            
    
