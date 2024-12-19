import math
class Solution:
    def isThree(self, n: int) -> bool:
        divisors = set()
        sqrtN = int(n ** (0.5))
        for i in range(1, sqrtN + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        
        return len(divisors) == 3
                