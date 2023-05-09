class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(sv,visited):
            if visited[sv]==-1:
                return False
            if visited[sv]==1: 
                return True
            visited[sv]=-1 
            for u in adj[sv]:
                if not dfs(u,visited):
                    return False 
            res.append(sv)  
            visited[sv]=1
            return True
        
        adj=[[] for i in range(numCourses)]
        res=[]
        for u,v in prerequisites:
            adj[v].append(u)
        visited=[0]*numCourses
        for i in range(numCourses):
            if not dfs(i,visited):
                return []
        return res[::-1]