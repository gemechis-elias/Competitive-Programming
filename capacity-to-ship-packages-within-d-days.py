class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_w = max(weights)
        max_w = sum(weights)
        ans = max_w
         
        while min_w < max_w:
            mid = (min_w + max_w)//2
            count = 0
            j = 0 
            sum_ = 0
            
            for j in range(len(weights)):
                if sum_ + weights[j] > mid:
                    sum_ = 0
                    count +=1
                
                sum_ += weights[j]

            count += 1
            if count <= days:
                max_w = mid
            else: 
                min_w = mid + 1
        
        return min_w