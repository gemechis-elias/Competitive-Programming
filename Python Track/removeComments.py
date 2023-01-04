class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        is_close = True
        tmp = "" 
        for idx, comment in enumerate(source):
            i = 0
            while i < len(comment):
                c = comment[i]
                if c in '/*':
                    if i+1 < len(comment) and comment[i:i+2] == '//' and is_close:
                        break
                    elif i+1 < len(comment) and comment[i:i+2] == '/*' and is_close:
                        is_close = False
                        i += 2
                        continue
                    elif i+1 < len(comment) and comment[i: i+2] == '*/' and not is_close:
                        is_close = True
                        i += 2
                        continue
                if is_close:
                    tmp += c
                i += 1
            if tmp != "" and is_close:
                res.append(tmp) 
                tmp = ""
        return res
