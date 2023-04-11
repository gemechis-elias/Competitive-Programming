class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dd = defaultdict(set)
        for i, j in roads:
            dd[i].add(j)
            dd[j].add(i)
        #print(dd)   
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                count = max(count, len(dd[i]) + len(dd[j]) - (i in dd[j]))        

        return count