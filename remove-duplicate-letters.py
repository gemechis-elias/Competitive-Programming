class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        hashMap = Counter(s)
        for i in range(len(s)):
            if s[i] in stack:
                hashMap[s[i]] -= 1

                if hashMap[s[i]] ==0:
                    del hashMap[s[i]]
                continue

            
            while stack and s[i] < stack[-1]:
                if stack[-1] in hashMap:
                    stack.pop()
                else:
                    break
            stack.append(s[i])

            hashMap[s[i]] -= 1

            if hashMap[s[i]] ==0:
                del hashMap[s[i]]
            print(stack, hashMap)
        return ''.join(stack)