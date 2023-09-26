class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        dp= []
        n = len(scores)
        for i in range(n):
            pairs.append([ages[i], scores[i]])
            
        pairs.sort()
        for u, v in pairs:
            dp.append(v)
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if pairs[j][1] >= pairs[i][1]:
                    dp[i] = max(pairs[i][1] + dp[j], dp[i])
            
        return max(dp)