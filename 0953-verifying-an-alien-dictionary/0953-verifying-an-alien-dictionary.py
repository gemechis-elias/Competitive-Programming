class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ord_d = {l:i for i, l in enumerate(order)}
         
        for w1, w2 in zip(words, words[1:]):
            for i, j in zip(w1, w2):
                if i != j:
                    if ord_d[i] > ord_d[j]: return False
                    break
            if w1.startswith(w2) and w1 != w2: return False
            
        return True