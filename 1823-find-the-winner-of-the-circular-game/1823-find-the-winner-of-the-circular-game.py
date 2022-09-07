class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(1, n + 1):
            winner = (winner + k)%i
            
        return (winner+1)
        # if n == 1:
        #     return 1
        
        # return ((findTheWinner(self, n - 1, k)) + k - 1)%n+1
#         players = []
#         while n > 0:
#             players.append(n)
#             n -= 1
#         players = players[::-1]
        
#         initial = 0
#         while len(players) > 1:
#             if initial == len(players) - 1:
#                 intial = -1
#                 tobeRemoved = initial + (k - 1)
#             tobeRemoved = initial + (k - 1)
#             print(tobeRemoved)
#             players.remove(players[tobeRemoved])
#             initial = tobeRemoved
            
#         print(players)
        