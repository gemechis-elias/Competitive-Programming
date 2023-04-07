class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashMap = {}
        
        for n in deck:
            hashMap[n] = 1 + hashMap.get(n, 0)
  
            
        arr = list(hashMap.values())
        res = arr[0]
        for i in range(1, len(arr)):
            res = math.gcd(res, arr[i])
 
        
        return all(arr[i] % res == 0  for i in range(len(arr))) and res != 1