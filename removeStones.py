class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rank = [1] * n
        parent = {}
        
        def union(x, y):
            x, y = representative(x), representative(y)

            if x == y:
                return 0
            if rank[x] < rank[y]:
                x, y = y, x
            rank[x] += rank[y]
            parent[y] = parent[x]
            return 1
        
        def representative(x):
            if x not in parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x])
            return parent[x]
        
        rows, cols = {}, {}
        removed = 0
        for i, (row, col) in enumerate(stones):
            if row in rows:
                removed += union(i, rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += union(i, cols[col])
            else:
                cols[col] = i
        
        return removed
