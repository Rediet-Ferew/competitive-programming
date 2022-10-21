class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            squares = 0
            while n:
                rem = n % 10
                rem = rem ** 2
                squares += rem
                n = n//10
            return squares
        hashSet = set()
        while n not in hashSet:
            hashSet.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        return False
    
            