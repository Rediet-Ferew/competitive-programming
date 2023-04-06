from collections import defaultdict
n = int(input())
graph = defaultdict(list)
cnt = 0
for i in range(n):
    
    row = list(map(int, input().split()))

    for j in range(len(row)):
        if row[j] == 1 and (j + 1) not in graph:
            graph[i + 1].append(j + 1)
            cnt += 1
        
print(cnt)
