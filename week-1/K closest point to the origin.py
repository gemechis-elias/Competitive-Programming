class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        list1=[]
        result=[0]*k
        
        for items in points:
            x= pow(items[0],2)
            y= pow(items[1],2)
            dis=(x+y)**(0.5)
            list1.append(dis)
            
        i=0
        
        while i<k:
        
            mini=min(list1[i:])
            ind=list1.index(mini,i)
            result[i]=points[ind]
            list1[i],list1[ind]=list1[ind],list1[i]
            points[i], points[ind]= points[ind], points[i]
            i+=1
            
        return result
