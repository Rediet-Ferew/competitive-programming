import math
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0: return self.isUgly(n//2)
        elif n % 3 == 0: return self.isUgly(n//3)
        elif n % 5 == 0: return self.isUgly(n//5)
        else: return False
        return True
        # if n <= 0:
        #     return False
        # primes = set()
        # num = n
        # while num % 2 == 0:
        #     primes.add(2)
        #     num = num/2
        # for i in range(3, int(math.sqrt(num))+1, 2):
        #     while num % i== 0:
        #         # print(i)
        #         primes.add(i)
        #         num = num / i
        # if num > 2:
        #     primes.add(int(num))
        # if len(primes) > 3:
        #     return False
        # else:
        #     for p in primes:
        #         if p not in [2,3,5]:
        #             return False
        # return True