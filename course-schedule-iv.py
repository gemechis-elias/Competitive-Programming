class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        incomming = [0] * numCourses
        
        for start ,end in prerequisites:
            graph[start].append(end)
            incomming[end] += 1
        
        qu = deque()
        for i in range(len(incomming)):
            if incomming[i] == 0:
                qu.append(i)
        ans = [set() for i in range(numCourses)]
        
        while qu:
            node = qu.popleft()
    
            for nbr in graph[node]:
                ans[nbr].add(node)
                for num in ans[node]:
                    if num not in ans[nbr]:
                        ans[nbr].add(num)
                
                incomming[nbr] -= 1
                if incomming[nbr]==0:
                    qu.append(nbr)
        res = [False] * len(queries)
        for i in range(len(queries)):
            if queries[i][0] in ans[queries[i][1]]:
                res[i] = True
        return res