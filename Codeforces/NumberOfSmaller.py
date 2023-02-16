n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
f = 0
s = 0

less_count = []
count = 0
while s < m:
    counter = 0
    while f < n and arr1[f] < arr2[s]:
        counter += 1
        f += 1
    count += counter
    less_count.append(count)
    s += 1
        
print(*less_count)
