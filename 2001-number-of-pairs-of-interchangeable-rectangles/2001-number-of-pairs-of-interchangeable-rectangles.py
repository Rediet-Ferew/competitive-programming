class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = {}
        n = len(rectangles)
        
        for i in range(n):
            w, h = rectangles[i]
            ratio = w/h
            ratio_count[ratio] = 1 + ratio_count.get(ratio, 0)
        pairs = 0
        for k, v in ratio_count.items():
            pair = (v*(v-1))//2
            pairs += pair
        return pairs