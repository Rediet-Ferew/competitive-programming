class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes = [True for k in range(right + 1)]
        primes[0] = False
        primes[1] = False
        i = 2
        while i <= right:
            if primes[i]:
                j = 2 * i
                while j <= right:
                    primes[j] = False
                    j += i
            i += 1
        primes = primes[left:]
        # print(primes)
        # cnt = 0
        ans = []
        for l in range(len(primes)):
            if primes[l] == True:
                ans.append(left + l)
        
        if len(ans) < 2:
            return [-1, -1]
        min_dis = float('inf')
        pairs = [-1, -1]
        for k in range(1, len(ans)):
            dis = ans[k] - ans[k - 1]
            if dis < min_dis:
                pairs[0] = ans[k - 1]
                pairs[1] = ans[k]
                min_dis = dis
        return pairs
