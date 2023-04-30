class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        arr=[-1]*n
        def dfs(node):
            for child in graph[node]:
                if arr[child-1]==-1:
                    if arr[node-1]==0:
                        arr[child-1]=1
                    else:
                        arr[child-1]=0
                    
                    if not dfs(child):
                        return False
                elif arr[child-1]==arr[node-1]:
                    return False
            return True
        for node,night in graph.items():
            if arr[node-1]==-1:
                arr[node-1]=0
                if not dfs(node):
                    return False
        return True
