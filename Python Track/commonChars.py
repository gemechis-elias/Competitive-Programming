class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        
        for a in words:
            res = res & collections.Counter(a)
            
        return list(res.elements())
