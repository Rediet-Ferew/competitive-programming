class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        days = []
        n = len(security)
        before = [0] * n
        before[0] = 1
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                before[i] = before[i - 1] + 1
            else:
                before[i] = 1
        after = [0] * n
        after[0] = 1
        for j in range(1, n):
            if security[j] >= security[j - 1]:
                after[j] = after[j - 1] + 1
            else:
                after[j] = 1    
        for k in range(time, n - time):
            if before[k] - before[k - time] == time and after[k + time] - after[k] == time:
                days.append(k)
        return days
        