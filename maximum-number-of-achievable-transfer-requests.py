class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        node_counts = [0] * n
        total_requests = len(requests)
        max_requests = 0
        
        def backtrack(i, count):
            nonlocal max_requests
            if i == total_requests:
                if all(c == 0 for c in node_counts):
                    max_requests = max(max_requests, count)
                    # print("up:", max_requests )

                return
            backtrack(i+1, count)
            
            node_counts[requests[i][0]] -= 1
            node_counts[requests[i][1]] += 1
            backtrack(i+1, count+1)

            node_counts[requests[i][0]] += 1
            node_counts[requests[i][1]] -= 1  
            # print(i, count, node_counts)
        backtrack(0, 0)
        return max_requests