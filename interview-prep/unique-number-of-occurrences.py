class Solution(object):
    def uniqueOccurrences(self, arr):
 
        freq = Counter(arr)
        values = list(freq.values())
        if len(set(values)) == len(values):
            return True

        