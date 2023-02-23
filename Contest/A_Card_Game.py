n = int(input())

cards = list(map(int, input().split()))

left = 0
right = n - 1
scores = []
while left <= right:
    
    if cards[left] >= cards[right]:
        scores.append(cards[left])
        left += 1
    elif cards[left] < cards[right]:
        scores.append(cards[right])
        right -= 1

serja = 0
dima = 0
for i in range(n):
    if i % 2 == 0:
        serja += scores[i]
    else:
        dima += scores[i]

print(serja, dima)
