n = int(input())
for i in range(n):
    size = input().split()
    x, y = size[0], size[1]
    if x[-1] == 'S' and y[-1] == 'M':
        print("<")
    elif x[-1] == 'M' and y[-1] == 'S':
        print(">")
    elif x[-1] == 'M' and y[-1] == 'L':
        print("<")
    elif x[-1] == 'L' and y[-1] == 'M':
        print(">")
    elif x[-1] == 'S' and y[-1] == 'L':
        print("<")
    elif x[-1] == 'L' and y[-1] == 'S':
        print(">")
    elif x[-1] == y[-1]:
        if x[-1] == 'M':
            print("=")
        elif x[-1] == "L":
            if len(x) == len(y):
                print("=")
            elif len(x) < len(y):
                print("<")
            else:
                print(">") 
        elif x[-1] == "S":
            if len(x) == len(y):
                print("=")
            elif len(x) < len(y):
                print(">")
            else:
                print("<") 
