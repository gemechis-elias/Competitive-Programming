class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        ans = []
        visited = set()
        for el,el1 in adjacentPairs:
            graph[el].append(el1)
            graph[el1].append(el)
            indegree[el] += 1
            indegree[el1] += 1
        queue = deque()
        for i in graph:
            if indegree[i] == 1:
                queue.append(i)
                break
        while queue:
            item = queue.popleft()
            ans.append(item)
            visited.add(item)
            for neigh in graph[item]:
                if neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
        return ans