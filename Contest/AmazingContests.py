n = int(input())

scores = list(map(int, input().split(" ")))

max_val = scores[0]
min_val = scores[0]
amazing_count = 0

for i in range(n):
    if scores[i] < min_val or scores[i] > max_val:
        amazing_count += 1
    max_val = max(max_val, scores[i])
    min_val = min(min_val, scores[i])
print(amazing_count)

        
