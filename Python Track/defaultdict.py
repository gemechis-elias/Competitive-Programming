# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
size_n, size_m = map(int, input().split())
ans = defaultdict(list)

for i in range (size_n):
    k = input()
    ans[k].append(str(i+1)) 
for i in range (size_m):
    j = input()
    if j in ans:
        str_ = " ".join(ans[j])
        print(str_)
    else:
        print(-1)
