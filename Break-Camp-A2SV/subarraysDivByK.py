class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        hashMap = defaultdict(int)
        hashMap[0] +=1

        prev = 0  
        for i in nums:
            prev += i
            answer += hashMap[prev % k]
            hashMap[prev % k] += 1

        return answer
    
    
    
