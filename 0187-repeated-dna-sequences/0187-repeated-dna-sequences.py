class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s = list(s)
        n = len(s)
        occurence = {}
        left = 0
        right = 9
        output = []
        while right <= n - 1:
            temp = s[left:right + 1]
            # temp.sort()
            temp = "".join(temp)
            if temp in occurence.keys():
                occurence[temp] += 1
            else:
                occurence[temp] = 1
            left += 1
            right += 1
        for key, val in occurence.items():
            if val > 1:
                output.append(key)
        return output
            