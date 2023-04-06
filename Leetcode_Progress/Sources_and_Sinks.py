n = int(input())

sources = set()
sinks = set()
zeros = set()
for i in range(n):
    row = list(map(int, input().split()))
    ones = 0
    for j in range(len(row)):
        if row[j] == 1:
            ones += 1
            sinks.add(j + 1)
    if ones > 0:
        sources.add(i + 1)
    
    elif ones == 0:
        zeros.add(i + 1)

zeros = zeros.difference(sources)
zeros = zeros.difference(sinks)
zr = list(zeros)
src = sources.difference(sinks)
snk = sinks.difference(sources)

src = list(src)
snk = list(snk)

src.extend(zr)
snk.extend(zr)

src = sorted(src)
snk = sorted(snk)
ans1 = [len(src)]
ans1.extend(src)
ans2 = [len(snk)]
ans2.extend(snk)

print(*ans1)
print(*ans2)
