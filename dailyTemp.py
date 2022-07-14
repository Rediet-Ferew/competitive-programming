class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counter = 0
        days = []
        if len(temperatures) <= 100000:
            for i in range(len(temperatures) - 1):
                for j in range(i + 1, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        counter = (j - i) 
                        break
                    else:
                        counter = 0
                days.append(counter)
            days.append(0)
            return days
                