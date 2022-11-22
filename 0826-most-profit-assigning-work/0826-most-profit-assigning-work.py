class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs = []
        for d, p in zip(difficulty, profit):
            pairs.append((d,p))
        pairs.sort()
        print(pairs)
        worker.sort()
        profit = 0
        l = 0
        max_profit = 0
        for i in range(len(worker)):            
            while l < len(pairs) and pairs[l][0] <= worker[i]:
                max_profit = max(max_profit, pairs[l][1])
                l += 1
            profit += max_profit
        return profit