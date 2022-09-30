def sortSentence(self, s: str) -> str:
    list1=[0]*(int(s.count(" ")+1))
    count=0
    result=""
    for ind in range(len(s)):
        if s[ind]==" ":
            list1[int(s[ind-1])-1]=s[count:ind-1]
            count=ind+1 
    list1[int(s[-1])-1]=s[count:-1]

    for i in range(len(list1)):
        if i != (len(list1)-1):
           result+=list1[i]+" "
        else:
            result+=list1[i]
    return result
