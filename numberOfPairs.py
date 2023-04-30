    def numberOfPairs(self, A, B, diff):
        l = SortedList()
        res = 0
        for a,b in zip(A, B):
            res += l.bisect_right(a - b + diff)
            l.add(a - b)
        return res
