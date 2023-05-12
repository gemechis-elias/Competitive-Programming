from typing import List
from collections import defaultdict

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(adj)):
            graph[i] = adj[i][:]
            
        visited = [0] * V 
        
        def dfs(node, parent):
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            
            return False
        
        for k in range(V):
            if visited[k] == 0:
                if dfs(k, -1):
                    return True
                
        return False

            
                
        
            
        
            
            
                
		
            
        
		    

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends