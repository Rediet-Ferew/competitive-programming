team_members =  int(input())
members = input().split(' ')
bad_flagged = input().split(' ')
excellent = 0

for i in range(team_members):
    
    if members[i] in bad_flagged:
        continue
    
    else:
        count = {}
        for ch in members[i]:
            count[ch] = 1 + count.get(ch, 0)
        if len(set(count.values())) == 1:
            excellent += 1
print(excellent)
