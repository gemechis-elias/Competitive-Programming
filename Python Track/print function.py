def function(n):
    ans = []
    for i in range(1,n+1):
        ans.append(str(i))
        answer = "".join(ans)
    return answer
if __name__ == '__main__':
    n = int(input())
    print(function(n))
        
