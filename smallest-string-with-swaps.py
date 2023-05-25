class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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

        n = len(s)
        parent = [i for i in range(n)]
        rank = [0] * n

        # Create disjoint sets based on the pairs
        for pair in pairs:
            union(parent, rank, pair[0], pair[1])

        # Group indices by their root parent
        groups = defaultdict(list)
        for i in range(n):
            groups[find(parent, i)].append(i)

        # Sort characters within each group
        sorted_chars = {}
        for group in groups.values():
            chars = sorted([s[i] for i in group])
            for i, char in zip(group, chars):
                sorted_chars[i] = char

        # Construct the smallest string
        smallest = [sorted_chars[i] for i in range(n)]

        return "".join(smallest)