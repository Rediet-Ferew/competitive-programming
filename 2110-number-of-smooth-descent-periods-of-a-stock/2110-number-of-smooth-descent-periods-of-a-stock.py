class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
#         days = 0
#         current = 1
#         newList = []
#         for i in range(1, len(prices)):
#             if prices[i - 1] - prices[i] == 1:
#                 current += 1
#             else:
#                 newList.append(current)
#                 current = 1
            
#             newList.append(current)
#             current = 1
#         for n in newList:
#             summation = ((n+1) * n) //2
#             days += summation
#         print(days)
        days = 0
        n = len(prices)
        i = 0
        while i < len(prices):
            j = i
            while j < len(prices) - 1 and prices[j + 1] + 1 == prices[j]:
                j += 1
            days += (j - i) * (j - i + 1) // 2
            i = j + 1
            
        days += len(prices)
        return days
                
        
        