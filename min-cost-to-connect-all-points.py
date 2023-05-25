class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, i, j):
            root_i = find(parent, i)
            root_j = find(parent, j)
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1

        def calculate_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        parent = [i for i in range(n)]
        rank = [0] * n
        edges = []
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                distance = calculate_distance(points[i], points[j])
                edges.append((distance, i, j))

        edges.sort()

        for edge in edges:
            distance, i, j = edge
            if find(parent, i) != find(parent, j):
                union(parent, rank, i, j)
                result += distance

        return result