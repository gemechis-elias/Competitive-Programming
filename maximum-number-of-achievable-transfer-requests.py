class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        node_counts = [0] * n
        total_requests = len(requests)
        self.max_requests = 0
        
        def backtrack(i, count):
            if i == total_requests:
                if all(c == 0 for c in node_counts):
                    self.max_requests = max(self.max_requests, count)
                return
            
            # Skip current request
            backtrack(i+1, count)
            
            # Perform current request
            node_counts[requests[i][0]] -= 1
            node_counts[requests[i][1]] += 1
            backtrack(i+1, count+1)
            node_counts[requests[i][0]] += 1
            node_counts[requests[i][1]] -= 1
            
        backtrack(0, 0)
        return self.max_requests