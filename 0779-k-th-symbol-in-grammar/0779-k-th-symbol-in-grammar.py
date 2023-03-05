class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recurssion(n, k):
            if n == 1:
                return 0
            
            else:
                s = (recurssion(n - 1, math.ceil(k/2)))
                
                # s = string[math.ceil(k/2)]
                if k % 2 == 0 and s == 1:
                    return 0
                elif k % 2 == 0 and s == 0:
                    return 1
                elif k % 2 != 0 and s == 1:
                    return 1
                elif k % 2 != 0 and s == 0:
                    return 0
        
        ans = recurssion(n, k)
        return ans
        # if ans == '1' and k % 2 != 0:
        #     print(1)
        # elif ans == '1' and k % 2 == 0:
        #     print(0)
        # if ans == '0' and k % 2 != 0:
        #     print(0)
        # elif ans == '0' and k % 2 == 0:
        #     print(1)
        