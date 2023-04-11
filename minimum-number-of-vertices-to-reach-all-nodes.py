class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = set()
        for u, v in edges:
            arr.add(v)
        return list(set(range(n)) - arr)