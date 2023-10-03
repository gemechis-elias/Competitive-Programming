class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def is_sub(word):
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True
        
        c=0
        for word in words:
            if is_sub(word):
                c+=1
        
        return c
        
