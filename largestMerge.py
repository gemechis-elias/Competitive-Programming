class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        ans = []
        left, right = 0,0
        while left < n and right < m:
            if ord(word1[left])>ord(word2[right]):
                ans.append(word1[left])
                left +=1
            elif ord(word1[left])<ord(word2[right]):
                ans.append(word2[right])
                right += 1
            else:
                if word1[left:len(word1)] > word2[right:len(word2)]:
                    ans.append(word1[left])
                    left +=1
                else:
                    ans.append(word2[right])
                    right += 1
        # --------------  
        if left < n:
            ans.extend(word1[left:])
        if right < m:
            ans.extend(word2[right:])
        s = ""  
        for i in ans:
            s += "".join(i)
        return s
