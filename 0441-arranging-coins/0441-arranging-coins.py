class Solution:
    def arrangeCoins(self, n: int) -> int:
        # k = 1
        # total = 0
        # while total <= n:
        #     total += k
        #     k += 1
        # return k - 2
        
        #binary search
        left = 1
        right = n 
        res = 0
        # if n == 1:
        #     return 1
        while left <= right:
            middle = (left + right)//2
            
            gaussian_sum = (middle * (middle + 1))//2
            
            if gaussian_sum > n:
                right = middle - 1
            else:
                if gaussian_sum == n:
                    return middle
                else:
                    
                    while middle <= right and gaussian_sum <= n:
                        middle += 1
                        gaussian_sum = (middle * (middle + 1))//2
                        
                    return middle - 1
                