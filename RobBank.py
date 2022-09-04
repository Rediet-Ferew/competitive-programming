class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        before = []
        
        n = len(security)
        for i in range(time, n - time):
            j = time
            k = time
            while j > 0:
                if security[i - j] >= security[i - j + 1]:
                    j -= 1
                else:
                    break
            while k > 0:
                if security[i + k] >= security[i + k - 1]:
                    k -= 1
                else:
                    break
            if j == 0 and k == 0:
                before.append(i)
        return before