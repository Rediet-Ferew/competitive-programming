class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        res = []
        score = 0
        right = 0
        while right < n:
            if s[right] == '(':
                stack.append(s[right])
                
                if score:
                    res.append(score)
                    score = 0
                right += 1
            else:
                i = right
                power = -1
                while stack and s[i] ==')':
                    stack.pop()
                    power += 1
                    i += 1
                # print(power)
                right = i
                score += 2 ** power
                if len(stack):
                    score *= 2 ** len(stack)
                # print(score)
        res.append(score)
        return sum(res)
            