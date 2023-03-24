
n, k = list(map(int, input().split()))

ratings =list(map(int, input().split()))

passed_round = []
def getWinner(left, right):
    mid = (left + right) // 2
    if right == left:
        return [(ratings[left], left)]
    
    left_winners = getWinner(left, mid)
    right_winners = getWinner(mid + 1, right)

    left_winners.sort()
    right_winners.sort()
    min_left = left_winners[0][0]
    min_right = right_winners[0][0]
    
    pass_round = []
    for i in range(len(right_winners)):
        
        diff =  min_left - right_winners[i][0]
        if diff <= k:
            
            pass_round.append(right_winners[i])
        
    for j in range(len(left_winners)):
       
        diff = min_right - left_winners[j][0]
        if diff <= k:
            
            pass_round.append(left_winners[j])
        
    return pass_round
        
ans = getWinner(0, len(ratings) - 1)

passed = [ans[idx][1] + 1 for idx in range(len(ans))]
passed.sort()

print(*passed)
        
            
    
