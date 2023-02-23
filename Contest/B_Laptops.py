n = int(input())
pairs = []

for _ in range(n):
    pair = list(map(int, input().split()))
    pairs.append(pair)

pairs.sort()
def checker(pairs):
    for idx in range(n - 1):
        p1, q1 = pairs[idx]
        p2, q2 = pairs[idx + 1]
        if q1 > q2:
            return("Happy Alex")
    return("Poor Alex")

print(checker(pairs))
