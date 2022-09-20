class Solution:
    def isPalindrome(self, s: str) -> bool:
        anothers = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                anothers += char
        anothers = anothers.lower()
        left = 0
        right = len(anothers) - 1
        while left < right:
            if anothers[left] != anothers[right]:
                return False
            left += 1
            right -= 1
        return True