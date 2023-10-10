class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        if sum(diff) < 0:
            return -1
        start = 0
        sum_ = 0
        idx = 0
        while start < len(gas):
            sum_ += diff[start]
            if sum_ < 0:
                sum_ = 0
                idx = start + 1
                
            start += 1
        return idx