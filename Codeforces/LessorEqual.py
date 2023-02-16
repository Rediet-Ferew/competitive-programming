n, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
less = -1
for idx in range(n):
    if nums[idx] > k:
        less = idx
        break
print(less)
