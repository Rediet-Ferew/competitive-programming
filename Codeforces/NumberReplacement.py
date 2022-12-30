test_cases = int(input())

def checkReplacement():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    letters = list(input())
    num_letter_pair = {}
    
    for i in range(n):
        
        if nums[i] not in num_letter_pair:
            num_letter_pair[nums[i]] = letters[i]
            
        else:
            
            if num_letter_pair[nums[i]] == letters[i]:
                continue
            else:
                print("NO")
                return
            
    print("YES")

for _ in range(test_cases):
    checkReplacement()
