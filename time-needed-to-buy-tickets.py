class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        idx = 0
        
        while tickets[k] != 0:
            if tickets[idx] > 0:
                tickets[idx] -= 1
                count += 1
            idx += 1
            if idx == len(tickets):
                idx = 0
        
        return count