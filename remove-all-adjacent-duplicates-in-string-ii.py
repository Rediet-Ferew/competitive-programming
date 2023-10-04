class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for idx, ch in enumerate(s):
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            if stack and stack[-1][1] == k:
                stack.pop()
        ans = ""
        for ch, num in stack:
            ans += (ch * num)
        return ans