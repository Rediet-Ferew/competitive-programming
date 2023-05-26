class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [0, 1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(1, math.ceil(n/2)):
            memo.append(memo[i])
            memo.append(memo[i] + memo[i + 1])
        
        memo.sort()
        return memo[-1]
        # return 3