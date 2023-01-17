test_cases = int(input())
def checker(rec1, rec2):
    
    rec1.sort()
    rec2.sort()
    if rec1[1] != rec2[1]:
        print("No")
        return
    one_side = rec1[0] + rec2[0]
    if one_side != rec1[1]:
        print("No")
        return
    print("Yes")
for _ in range(test_cases):
    
    rec1 = list(map(int, input().split()))
    rec2 = list(map(int, input().split()))
    checker(rec1, rec2)
        
    
            
