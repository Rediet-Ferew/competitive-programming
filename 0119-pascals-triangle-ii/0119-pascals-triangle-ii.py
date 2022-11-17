class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        for _ in range(rowIndex):
            row = [1] * (len(dp[-1]) + 1)
            for i in range(1,len(row)-1):
                row[i] = dp[-1][i-1] + dp[-1][i]
            dp.append(row)
        return dp[-1]