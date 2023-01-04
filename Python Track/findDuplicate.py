class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap={}
        for path in paths:
            temp=path.split(" ")
            current=[]
            for i in range(1,len(temp)):
                content=temp[i].split("(")
                file_=hashmap.get(content[1],-1)
                if file_ == -1:
                    file_=[]
                    file_.append(temp[0]+"/"+content[0])
                    hashmap[content[1]]=file_
                else:
                    file_.append(temp[0]+"/"+content[0])
                    hashmap[content[1]]=file_
        result=[value for value in hashmap.values() if len(value)>1] 
        return result
