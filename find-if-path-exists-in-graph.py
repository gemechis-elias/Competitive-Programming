class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        parent = {}
        rank = [1]  * (n+1)
        
        def representative(x):
            if x not in parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x])
            return parent[x]

        def union(x, y):
            x_root = representative(x)
            y_root = representative(y)

            if rank[x_root] > rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] <= rank[y_root]:
                parent[y_root] = x_root

        def connected(x, y):
            return representative(x) == representative(y)
        
        for a,b in edges:
            union(a,b)
        
        return connected(source,destination)