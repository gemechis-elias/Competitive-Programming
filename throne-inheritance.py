class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = kingName
        self.alive = {}
        self.alive[kingName] = 0
        self.edges = {self.root:[]}
        
    def birth(self, parentName: str, childName: str) -> None:
        self.alive[childName] = self.alive[parentName]+1
        if parentName in self.edges:
            self.edges[parentName].append(childName)
            if childName not in self.edges:
                self.edges[childName] = []
        else:
            if childName not in self.edges:
                self.edges[childName] = []
            self.edges[parentName] = [childName]
            
    def death(self, name: str) -> None:
        del self.alive[name]
        
    def getInheritanceOrder(self) -> List[str]:
        hierarchy = []
        def dfs(cur,parent=-1):
            nonlocal hierarchy
            if cur in self.alive:
                hierarchy.append(cur)
            for i in self.edges[cur]:
                if i!=parent:
                    dfs(i,cur)
        dfs(self.root)
        return hierarchy