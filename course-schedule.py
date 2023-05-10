class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cnt=defaultdict(int)
        graph=defaultdict(list)
        que=deque()
        
        for i,j in prerequisites:
            graph[j].append(i)
            cnt[i]+=1
        for i in range(numCourses):
            if cnt[i]==0:
                que.append(i)
 
        ans=[]           
        while que:
            curr=que.popleft()
            ans.append(curr)
            
            for nigh in graph[curr]:
                cnt[nigh]-=1
                if cnt[nigh]==0:
                    que.append(nigh)
                    
        return True if len(ans)==numCourses else False