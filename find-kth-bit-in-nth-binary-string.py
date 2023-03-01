class Solution:
    def findKthBit(self, n: int, k: int, s="0") -> str:

        def invert(s):
            arr = [x for x in s]
            for i in range(len(arr)):
                if arr[i] == "1":
                    arr[i] = "0"
                elif arr[i] == "0":
                    arr[i] = "1"
            ans = "".join(arr)

            return ans
        #base case 
        if n == 0:
            return s[k-1]
            
        rev = invert(s)
        s = s + "1" + rev[::-1]
        return self.findKthBit(n-1, k, s )