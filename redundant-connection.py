class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1, len(edges)+1)}
        print(parent)

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
                return parent[u]
            else:
                return u
        def union(u, v):
            rep_of_u = find(u)
            rep_of_v = find(v)
            if rep_of_u == rep_of_v:
                return True
            else:
                parent[rep_of_u] = rep_of_v
                return False
        redundant = []

        for u, v in edges:
            if union(u, v):
                redundant = [u, v]
            if redundant == [u, v]:
                break
        return redundant