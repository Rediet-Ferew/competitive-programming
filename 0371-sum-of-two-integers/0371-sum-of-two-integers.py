class Solution:
    def getSum(self, a: int, b: int) -> int:
        import math
        if b >= 0:
            while b > 0:
                a += 1
                b -= 1
        else:
            while b < 0:
                a -= 1
                b += 1
        return a
        # return int(math.log(math.exp(a) * math.exp(b)))