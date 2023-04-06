class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        len_max = 0
        
        word_sets = [set(word) for word in words]

        for i in range(n):
            for j in range(i+1, n):
                if not (word_sets[i] & word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    len_max = max(len_max, product)

        return len_max