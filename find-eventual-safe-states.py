class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True
        
        n = len(graph)
        visited = [0] * n
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res