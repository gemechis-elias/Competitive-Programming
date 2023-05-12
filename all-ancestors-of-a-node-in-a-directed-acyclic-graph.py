class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        inDegree = [0] * n

        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].append(end)
            inDegree[end] += 1
        output = [set() for _ in range(n)]        
        queue = deque()

        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)
                
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for desc in graph[node]:
                    output[desc].add(node)
                    for anc in output[node]:
                        output[desc].add(anc)
                    inDegree[desc] -= 1
                    if inDegree[desc] == 0:
                        queue.append(desc)
        for i in range(n):
            output[i] = sorted(list(output[i]))
        return output