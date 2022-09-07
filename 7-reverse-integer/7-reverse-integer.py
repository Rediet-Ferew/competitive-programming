class Solution:
    def reverse(self, x: int) -> int:
        num = x
        nums = []
        if num == 0:
            return 0
        if num > 0:
            while num > 0:
                nums.append(num % 10)
                num = num // 10
            xStr = ''.join(str(n) for n in nums)
        elif num < 0:
            num = -1 * num
            xStr = '-'
            while num > 0:
                nums.append(num % 10)
                num = num // 10
            xStr += ''.join(str(n) for n in nums)
        if int(xStr) not in range((-2)**31, 2**31 - 1):
            return 0
        else:
            return int(xStr)
            