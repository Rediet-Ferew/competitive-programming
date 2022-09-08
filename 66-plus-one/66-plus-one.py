class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        for i in range(0, n):
            val = digits.pop()
            num += (val * (10**i))
        num = num + 1
        final = [int(k) for k in str(num)]
        return final
            