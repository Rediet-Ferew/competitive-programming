class Solution:
    def isPalindrome(self, s: str) -> bool:
        anothers = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                anothers += char
        anothers = anothers.lower()
        if anothers == anothers[::-1]:
            return True
        else:
            return False