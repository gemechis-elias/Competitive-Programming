class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap=dict()
        nums.sort()
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] =1

        count=0

        for i in nums:
            if hashmap[i]>0 and (k-i) in hashmap and  hashmap[k-i]> 0 :
                hashmap[i]-=1
                if hashmap[k-i]> 0:
                    hashmap[k-i]-=1
                    count+=1
        return count
