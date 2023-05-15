class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_count = [0 for _ in range(len(quiet))]
        graph = defaultdict(list)
        answer = [idx for idx in range(len(quiet))]
        
        ## create the graph so that we go from the richer to the poorer
        for rich, poor in richer:
            graph[rich].append(poor)
            richer_count[poor] += 1
            
        ## we include the richest ones.
        queue = collections.deque([])
        for person, rich_count in enumerate(richer_count):
            if not rich_count:
                queue.append(person)
                
        while queue:
            person = queue.popleft()
            ## pointer to the quietest person
            quieter_person = answer[person]
            
            for poorer in graph[person]:
                ## pointer to the quietest person richer than me
                quieter_richer = answer[poorer]
                ## on the answer we are storing the pointer to the quietest one. so for the next poorer we are going to store the pointer which contains the quietest
                answer[poorer] = min(quieter_person, quieter_richer, key = lambda prsn : quiet[prsn])
                richer_count[poorer] -= 1
                if not richer_count[poorer]:
                    queue.append(poorer)
        return answer