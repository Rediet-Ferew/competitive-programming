from collections import defaultdict
n_nodes = int(input())
ops = int(input())

graph = defaultdict(list)
neighbors = []
for i in range(ops):
    op = list(map(int, input().split()))
    if len(op) == 3:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    else:
        neighbors.extend(graph[op[1]])
print(*neighbors)
