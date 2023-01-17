test_cases = int(input())

for i in range(test_cases):
    
    phrases = input().split(' ')
    ordered = []
    
    for word in phrases:
        for letter in word:
            
            if letter.isnumeric():
                
                ordered.append([letter, word.replace(letter, "")])
                break
    final = sorted(ordered)
    ans = []
    for pair in final:
        ans.append(pair[1])
    print(" ".join(ans))
    
