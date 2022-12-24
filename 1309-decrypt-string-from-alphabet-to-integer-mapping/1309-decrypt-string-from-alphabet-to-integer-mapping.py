class Solution:
    def freqAlphabets(self, s: str) -> str:
        # "10#11#12"
        
        alphabet = "0abcdefghijklmnopqrstuvwxyz"
        result = ""
        temp =""
        for i in s: 
            if i != "#":
                j = int(i)
                result += alphabet[j]
                temp += i
            else:
                last_two = ""
                last_two +=  temp[len(temp)-2:]
                result = result[:len(result)-2]
                x = int(last_two)
                result = result + alphabet[x]
        return result
                
                
                
        
                



                

            