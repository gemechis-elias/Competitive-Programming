from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for k, v in edges:
            dic[k].append(v)
            dic[v].append(k)

        print(dic)
        visited = set()

        def dfs(node):
            if node == destination: 
                return True
            
            visited.add(node)
            for node in dic[node]:
                if node not in visited:
                    if dfs(node):
                        return True
               


        return dfs(source)