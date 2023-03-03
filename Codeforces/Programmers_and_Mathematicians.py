test_cases = int(input())

def getMaxTeams(p, m, max_range):
    
    start = 0
    end = max_range
    max_team = 0
    
    while start <= end:
        
        mid = (start + end) // 2
        remaining = p - mid + m - mid
        
        if remaining > 2 * mid:
            start = mid + 1
            max_team = mid

        elif remaining < 2 * mid:
            end = mid - 1
        
        else:
            return mid
    
    return max_team

for _ in range(test_cases):
    
    a, b = list(map(int, input().split()))
    max_teams = getMaxTeams(a, b, min(a, b))
    print(max_teams)
