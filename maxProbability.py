from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:       
        # build graph
        graph = defaultdict(list)
        for (u,v), probability in zip(edges, succProb):
            graph[u].append([v, probability])
            graph[v].append([u, probability])

      
        pq = [[-1, start]]
        visited = set()

        while pq:
            prob, node = heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return -prob  # maximum probability , don't forget the - here !        
            for adj_node, path_prob in graph.get(node, []):
                heappush(pq, [prob * path_prob, adj_node]) 
        return 0 # end node not found
