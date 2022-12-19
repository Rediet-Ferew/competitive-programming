# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    n = int(input())
    cubes = input().split(" ")
    def piler():
        stack = []
        l = 0
        r = len(cubes) - 1
        while l < r:
            if int(cubes[r]) >= int(cubes[l]):
                if not stack or stack and stack[-1] >= int(cubes[r]):
                    stack.append(int(cubes[r]))
                else:
                    return "No"
                r -= 1
            else:
                if not stack or stack and stack[-1] >= int(cubes[l]):
                    stack.append(int(cubes[l]))
                else:
                    return "No"
                l += 1
        return "Yes"
    print(piler())
    
          
