class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        n = len(s)
        for c in s:
            temp = []
            if c.isalpha():
                for r in result:
                    temp.append(r + c.lower())
                    temp.append(r + c.upper())
            else:
                for r in result:
                    temp.append(r + c)
            result=temp
        return result