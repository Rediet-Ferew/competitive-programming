class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        firstPart = sorted(changed[: len(changed)//2])
        secondPart = sorted(changed[(len(changed)//2):])
        
        
        if len(firstPart) == len(secondPart):
            for x, y in zip(firstPart, secondPart):
                if y == 2 * x:
                    return firstPart
                elif x == 2 * y:
                    return secondPart
                else:
                    return []
        else:
            return []