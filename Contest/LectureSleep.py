n, k = list(map(int, input().split(' ')))
lectures = list(map(int, input().split(' ')))
t = list(map(int, input().split(' ')))

left = 0
right = 0
prefix = 0
awake = 0

for i in range(n):
    
    if t[i] == 1:
        awake += lectures[i]
        
while right < k:
    
    if t[right] == 0:
        prefix += lectures[right]
    right += 1

max_lecture = prefix
            
while right < n:
    if t[left] == 0:
        prefix -= lectures[left]
    left += 1
    
    if t[right] == 0:
        prefix += lectures[right]
    right += 1
    
    max_lecture = max(max_lecture, prefix)
    
print(awake + max_lecture)

