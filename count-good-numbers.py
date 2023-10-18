class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10 ** 9) + 7
        evens, primes = 0, 0
        if n % 2 == 0:
            evens = n // 2
            primes = n // 2
        else:
            evens = (n // 2) + 1
            primes = n // 2
        ans = pow(4, primes, mod) * pow(5, evens, mod)
        return ans % mod
        # def recursion(num, n):
        #     print(f"Calling recursion({num}, {n})")
        #     if n == 0:
        #         print("Base Reached")
        #         return 1
            
        #     if n % 2 == 0:
        #         result = recursion((num * num) % mod, n // 2)
        #         print(f"Returning result: {result}")
        #         return result
        #     else:
        #         result = num * recursion((num * num) % mod, (n - 1) // 2)
        #         print(f"Returning result: {result}")
        #         return result
        
        # # return ((recursion(5 ,evens) % mod) * (recursion(4, primes)) % mod
        # recursion(4, 8) % mod