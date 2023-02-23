n = int(input())
nums = list(map(int, input().split()))

neg_count = 0
zero_count = 0
coins = 0
for idx, num in enumerate(nums):
    if num < 0:
        diff = abs(num) - 1
        coins += diff
        neg_count += 1
    elif num > 0:
        diff = num - 1
        coins += diff
    else:
        coins += 1
        zero_count += 1

if neg_count % 2 != 0 and not zero_count:
    coins += 2

print(coins)
