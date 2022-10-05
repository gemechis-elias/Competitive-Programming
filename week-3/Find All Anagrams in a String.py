class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        map = Counter(p)
        distincts = len(map)
        i,j = 0,0
        k = len(p)
        while(j < len(s)):
            if s[j] in map:
                map[s[j]] -= 1
                if(map[s[j]] == 0): distincts -= 1
            if(j - i + 1 < k): j += 1
            else:
                if(distincts == 0): answer.append(i)

                if s[i] in map: 
                    map[s[i]] += 1
                    if(map[s[i]] == 1): distincts += 1
                i += 1
                j += 1

        return answer
