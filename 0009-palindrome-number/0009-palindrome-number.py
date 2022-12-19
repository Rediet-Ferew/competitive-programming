class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        n = x
        while n > 0:
            reverse = (reverse*10) + (n%10)
            n = n//10
        if x == reverse: return True
        else: return False