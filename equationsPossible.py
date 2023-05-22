class UnionFind:
    def __init__(self):
        self.parent = list(range(26))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        
        # Perform union for all equality equations
        for equation in equations:
            if equation[1] == "=":
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                uf.union(x, y)
        
        # Check for inconsistencies in inequality equations
        for equation in equations:
            if equation[1] == "!":
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False
        
        return True
