from collections import *

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for  i in range(n):
            indeg[i+1] = 0
        
        for u,v in edges:
            graph[u].append(v)
            indeg[v] += 1
        
        qu = deque()
        for key,val in indeg.items():
            if val == 0:
                qu.append([key,1])
                
        times = [0]*n
        while qu:
            node,time = qu.popleft()
            times[node-1] = time
            for nbr in graph[node]:
                indeg[nbr] -= 1
                if indeg[nbr]==0:
                    qu.append([nbr,time+1])
        return ' '.join(map(str,times))
