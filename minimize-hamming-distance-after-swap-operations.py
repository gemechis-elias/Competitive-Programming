class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        parent = defaultdict(int)
        for i in range(len(source)):
            parent[i]=i
        rank=[0 for i in range(len(source))]
        def find(x):
            root=x
            while root!=parent[root]:
                root=parent[root]
            
            while x!=root:
                temp=parent[x]
                parent[x]=root
                x=temp
            return root
            
        def union(x,y):
            parentX=find(x)
            parentY=find(y)
            if parentX==parentY:return
            
            if rank[parentX]==rank[parentY]:
                rank[parentX]+=1
            if rank[parentX]>rank[parentY]:
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
        for index1, index2 in allowedSwaps:
            union(index1, index2)

        swappable_indices = defaultdict(list)
        for i in range(len(source)):
            swappable_indices[find(i)].append(i)

        ans = 0
        for indices in swappable_indices.values():
            source_group = [source[i] for i in indices]
            target_group = [target[i] for i in indices]
            source_count = defaultdict(int)
            target_count = defaultdict(int)

            for num in source_group:
                source_count[num] += 1
            for num in target_group:
                target_count[num] += 1

            for num, count in source_count.items():
                diff = count - target_count[num]
                if diff > 0:
                    ans += diff

        return ans