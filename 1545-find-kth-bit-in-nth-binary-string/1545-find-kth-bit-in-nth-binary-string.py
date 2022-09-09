class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        stack = ["0"]
        for i in range(1, n):
            inverted = ''.join(['1' if i == '0' else '0'
                     for i in stack[i - 1]])
            newStr = str(stack[i - 1]) + "1" + inverted[:: -1]
            stack.append(newStr)
        return stack[n - 1][k - 1]
        