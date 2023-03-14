class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons
        self.vote_sum = []
        self.votes = defaultdict(int)
        self.n = len(persons)
        self.max_vote = 0
        for i in range(self.n):
            self.votes[self.persons[i]] += 1
            if not self.vote_sum:
                self.vote_sum.append(self.persons[i])
                self.max_vote = 1
            elif self.votes[self.persons[i]] >= self.max_vote:
                self.vote_sum.append(self.persons[i])
                self.max_vote = self.votes[self.persons[i]]
            else:
                self.vote_sum.append(self.vote_sum[-1])
    def q(self, t: int) -> int:
        r = bisect_right(self.times, t)
        return self.vote_sum[r - 1]
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)