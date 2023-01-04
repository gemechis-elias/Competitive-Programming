# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(input().split())
sets_ = set()
n = int(input())
strict = True
for i in range(n):
    set_ = set(input().split())
    for i in set_:
        if i not in set_a:
            strict = False
            break
if strict:
    print("True")
else:
    print("False")
