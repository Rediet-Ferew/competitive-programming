class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factorization = set()
        def checkIsPrime(n):
            
            
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.add(n)
        for num in nums:
            checkIsPrime(num)
        return len(factorization)
            
