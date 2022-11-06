class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        def paint(image: List[List[int]], sr: int, sc: int, color: int, oldColor : int):
            if sr >= r or sc >= c or sr < 0 or sc < 0 or image[sr][sc] != oldColor:
                return;
            image[sr][sc] = color
            paint(image, sr - 1, sc, color, oldColor)
            paint(image, sr + 1, sc, color, oldColor)
            paint(image, sr, sc - 1, color, oldColor)
            paint(image, sr, sc + 1, color, oldColor)
        
        
        if image[sr][sc] == color: return image
        paint(image, sr, sc, color, image[sr][sc])
        return image
        