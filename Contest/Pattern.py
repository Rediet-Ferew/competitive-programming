n = int(input())
p = input()
p_len = len(p)
patterns = []

for j in range(len(p)):
    patterns.append(set(p[j]))

for i in range(n - 1):
    pattern = input()
    for j in range(p_len):
        patterns[j].add(pattern[j])
        
     
ans = [""] * p_len

for k in range(p_len):
    intersect = patterns[k]

    if len(intersect) == 1 and "?" in intersect:
        ans[k] = "x"
    
    elif len(intersect) == 1 and "?" not in intersect:
        temp = list(intersect)
        ans[k] = temp[0]
    
    elif len(intersect) == 2:
        temp = list(intersect)
        if temp[0] != temp[1] and temp[0] != "?" and temp[1] != "?":
            ans[k] = "?"
        else:
            ans[k] = temp[0] if temp[0] != "?" else temp[1]
    
    elif len(intersect) > 2:
        ans[k] = "?"
            
print("".join(ans))
