class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        total_requests = len(requests)
        self.max_requests = 0
        
        for mask in range(1 << total_requests):
            node_counts = [0] * n
            count = 0
            
            for i in range(total_requests):
                if mask & (1 << i):
                    node_counts[requests[i][0]] -= 1
                    node_counts[requests[i][1]] += 1
                    count += 1
                    
            if all(c == 0 for c in node_counts):
                self.max_requests = max(self.max_requests, count)
            
        return self.max_requests