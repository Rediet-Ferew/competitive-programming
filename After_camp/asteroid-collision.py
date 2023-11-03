class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        
        for i in range(n):
            # print(asteroids[i])
            # print(stack)
            if not stack:
                stack.append(asteroids[i])
            elif asteroids[i] > 0:
                stack.append(asteroids[i])
            elif asteroids[i] < 0:
                if stack and stack[-1] < 0:
                    stack.append(asteroids[i])
                
                elif stack and stack[-1] > 0:
                    
                    while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                    # print(stack, asteroids[i])
                    if stack and (stack[-1] == abs(asteroids[i])):
                        stack.pop()
                    elif not stack or stack[-1] < 0:
                        stack.append(asteroids[i])
                    


        
        return stack

                
            
