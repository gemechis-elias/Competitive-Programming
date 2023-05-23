class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)} 
    
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        all_emails = dict()
        un = UnionFind(len(accounts))

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in all_emails:
                    un.union(all_emails[email], i)
                    continue
                
                all_emails[email] = i
        ac_em = dict()
        for email in all_emails:
            acc = un.find(all_emails[email])
            
            if acc in ac_em:
                ac_em[acc].append(email)
            else:
                ac_em[acc] = [email]
             
        res = []   
        for p in ac_em:
            res.append([accounts[p][0]] + sorted(ac_em[p]))
        # print(all_emails, ac_em)
        return res