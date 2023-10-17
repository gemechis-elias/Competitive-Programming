import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        grid=[[] for i in range(n)]
        for frm,to,cst in flights:
            grid[frm].append((cst,to))
        
        st=[(0,0,src)]
        heapq.heapify(st)
        css=[(float("infinity"),float("infinity"))]*n
        css[src]=(0,0)
        while st:
            cst,stop,x=heapq.heappop(st)
            if x==dst:
                return cst
            if stop<=k:
                for ct,to in grid[x]:
                    if css[to][0]>ct+cst or css[to][1]>stop+1:
                        css[to]=(ct+cst,stop+1)
                        heapq.heappush(st,(cst+ct,stop+1,to))

        return -1