 def fizzBuzz(self, n: int) -> List[str]:
        mylist=['Fizz','Buzz','FizzBuzz']
        outputlist=[]
        for x in range(1,n+1):
            
            if x%5==0 and i%3==0:
                outputlist.append(mylist[2]) 
            elif x%3==0:
                outputlist.append(mylist[0])
            elif x%5==0:
                outputlist.append(mylist[1])
        
            else:
                outputlist.append(str(x))
        return outputlist
