class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        to_be_joined = []
        prev = 0
        
        for i in range(len(spaces)):

            to_be_joined.append(s[prev:spaces[i]])
            prev = spaces[i]
        to_be_joined.append(s[prev:])

        return " ".join(to_be_joined)
