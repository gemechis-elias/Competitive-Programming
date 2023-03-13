class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = [0] * len(times)
        self.leader = persons[0]
        self.vote = defaultdict(int)
        
        for i in range(len(times)):
            self.vote[persons[i]] += 1
            if self.vote[persons[i]] >= self.vote[self.leader]:
                self.leader = persons[i]
            self.leaders[i] = self.leader

    def q(self, t: int) -> int:
        idx = bisect_left(self.times, t)
        
        if idx < len(self.times) and self.times[idx] == t:
            return self.leaders[idx]
        else:
            return self.leaders[idx - 1]
         


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)