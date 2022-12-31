import re
 
def num_sort(test_string):
    return list(map(int, re.findall(r'\d+', test_string)))[0]
    
n= int(input())
ans =""
for i in range(n):
    words = input().split()
    
    words.sort(key=num_sort)
    
    for word in words:
        ans += "".join([i for i in word if not i.isdigit()]) + " " 
        
    ans = ans[:-1]+"\n"  #just remove for space from last sentence
print(ans)
