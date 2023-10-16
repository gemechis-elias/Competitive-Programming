from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for eq,val in zip(equations,values):
            graph[eq[0]][eq[1]]=val
            graph[eq[1]][eq[0]]=1/val
        
        return [calculate(q[0],q[1],graph,1.0,set()) for q in queries]
        



def calculate(dividend,divisor,graph,k,visited):
    if divisor in graph[dividend]:
        return k*graph[dividend][divisor]
    for neighbour in graph[dividend]:
        if neighbour not in visited:
            visited.add(neighbour)
            result = calculate(neighbour,divisor,graph,k*graph[dividend][neighbour],visited)
            if result != -1.0:
                return result
    return -1.0