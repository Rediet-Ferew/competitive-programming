class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        
        for _ in range(numRows - 1):
            row = [1] * (len(dp[-1]) + 1)
            for i in range(1,len(row)-1):
                row[i] = dp[-1][i-1] + dp[-1][i]
            dp.append(row)
        return dp
                