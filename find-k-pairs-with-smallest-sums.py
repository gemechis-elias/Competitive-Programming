class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                p = [nums1[i],nums2[j]]
                if len(res)<k:
                    heapq.heappush(res,[-(nums1[i]+nums2[j]),p])
                else:
                    if nums1[i]+nums2[j]>-res[0][0]:
                        break
                    heapq.heappush(res,[-(nums1[i]+nums2[j]),p])
                    heapq.heappop(res)
        
        ans = []
        for i in range(len(res)):
            ans.append(res[i][1])
        
        return ans