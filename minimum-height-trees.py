class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        cnt=n
        graph=defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leave=[node for node in graph if len(graph[node])==1]

        while cnt>2:
            cnt-=len(leave)
            
            leave_node=[]
            
            for i in leave:
                nigh=graph[i].pop()
                graph[nigh].remove(i)
                
                if len(graph[nigh])==1:
                    leave_node.append(nigh)
                leave=leave_node

        return leave