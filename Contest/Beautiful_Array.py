n = int(input())

nums = list(map(int, input().split(" ")))
nums.sort()

neg = []
pos = []
zero = []
for n in nums:
    if n < 0:
        neg.append(n)
    elif n > 0:
        pos.append(n)
    else:
        zero.append(n)
if len(neg) % 2 == 0:
    zero.append(neg.pop())
if not pos:
    pos.append(neg.pop())
    pos.append(neg.pop())
print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)
