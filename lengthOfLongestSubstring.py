class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        left =  0
        ans = 0
        for i in range(len(s)):
            hashMap[s[i]] = hashMap.get(s[i], 0) + 1
            while hashMap.get(s[i]) >1:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                left +=1
            ans = max(ans, len(hashMap))
        return ans

            
            
            
