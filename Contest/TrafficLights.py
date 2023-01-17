#number of test cases
test_cases = int(input())

def secondFinder():
    #Accepting inputs
    n, ch = input().split(' ')
    lights = input()
    n = len(lights)
   
    #append the lights for cycle iteration
    lights += lights
    res = 0
    greens = []
    
    #store all g indices in the cycle
    for i in range(2*n):
        if lights[i] == 'g':
            greens.append(i)
    
    #iterate through the given input to find the possible current on lights
    for j in range(n):
        
        if lights[j] == ch:
            ix = j
            
            #find the first g index greater than the current letter
            for idx in range(len(greens)):
                #calculate the max distance for currently on color 
                if greens[idx] >= ix:
                    res = max(res, greens[idx] - j)
                    break
            
    print(res)
    
for i in range(test_cases):
    #call the function
    secondFinder()
    
