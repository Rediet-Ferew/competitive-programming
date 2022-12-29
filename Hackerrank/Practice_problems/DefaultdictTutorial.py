# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = list(map(int, input().split(' ')))
group_A = defaultdict(list)

for i in range(n):
    item = input()
    group_A[item].append(i + 1)
for _ in range(m):
    item = input()
    if item in group_A:
        print(*group_A[item])
    else:
        print(-1)
