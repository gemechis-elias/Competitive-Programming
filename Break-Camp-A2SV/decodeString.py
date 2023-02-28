class Solution:
    def decodeString(self, s: str) -> str:
        def decodeHelper(s, i):
            res = ""
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    decodedStr, i = decodeHelper(s, i + 1)
                    res += num * decodedStr
                    print(res)
                    num = 0
                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]
                i += 1
            
            return res

        return decodeHelper(s, 0)



