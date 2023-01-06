class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d= Counter()
        count=0
        for current_word in words:
            word="".join((set(current_word)))
            count+=d[word]
            d[word]+=1
        return count