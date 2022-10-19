class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [num for num in range(1,n+1)]
        def findWinner(arr, start, k):
            if len(arr)==1:
                # return array[0]
                return
            start=(start + k)%len(arr)
            arr.pop(start)
            # return findWinner(array,start,k)
            findWinner(arr,start,k)
        findWinner(arr,0,k-1)
        return arr.pop()
