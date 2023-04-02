class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        n = len(nums)
        max_num = max(nums)
        min_num = min(nums)
        g_cd = gcd(max_num, min_num)
        return g_cd
