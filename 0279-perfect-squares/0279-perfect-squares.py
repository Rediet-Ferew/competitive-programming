class Solution:
    def numSquares(self, n: int) -> int:
        import math
        #according to lagranges theorem, there are 4 solutions to the problem
        #1,2,3,4
        #if the number is a perfect square
        def isPerfectSq(num):
            root = math.sqrt(num)
            root = int(root)
            if root* root == num:
                return True
            return False
        if isPerfectSq(n): return 1
        #check if n - (i*i) is a perfect square
        #if yes, answer is 2, which is (i*i) + n-(i*i)
        sqRoot = int(math.sqrt(n))
        for i in range(1, sqRoot+1):
            if isPerfectSq(n - (i*i)):
                return 2
        # ans = 3
        # possible if the number is not representable in the form
        # 4^a (8*b + 7)
        while not n%4: 
            n//=4                        
        if n%8 != 7: 
            return 3 
        #if all above is not true
        return 4