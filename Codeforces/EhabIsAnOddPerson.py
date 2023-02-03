n = int(input())
nums = list(map(int, input().split()))

even_count = 0
odd_count = 0

for idx, num in enumerate(nums):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if not even_count or not odd_count:
    print(*nums)
else:
    nums.sort()
    print(*nums)
