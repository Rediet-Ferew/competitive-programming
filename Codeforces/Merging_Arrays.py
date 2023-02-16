n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
f = 0
s = 0
merged = []

while f < n and s < m:
    
    if arr1[f] <= arr2[s]:
        merged.append(arr1[f])
        f += 1
    else:
        merged.append(arr2[s])
        s += 1

while f < n:
    merged.append(arr1[f])
    f += 1

while s < m:
    merged.append(arr2[s])
    s += 1
print(*merged)
    
