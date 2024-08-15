class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        
        for i in range(len(bills)):
            if bills[i] == 5:
                d[5] += 1
            elif bills[i] == 10:
                d[10] += 1
                if d[5] > 0:
                    d[5] -= 1
                else:
                    return False
            else:
                d[20] += 1
                if d[5] > 0 and d[10] > 0:
                    d[5] -= 1
                    d[10] -= 1
                elif d[5] >= 3:
                    d[5] -= 3

                else:
                    return False
        return True
                    