class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = []
        n = len(names)
        
        for k in range(n):
            for idx in range(n - 1):
                if heights[idx] < heights[idx + 1]:
                    heights[idx], heights[idx + 1] = heights[idx + 1], heights[idx]
                    names[idx], names[idx + 1] = names[idx + 1], names[idx]

        

        return names