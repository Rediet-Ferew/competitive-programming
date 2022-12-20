class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_manhattan = float('inf')
        idx = -1
        for i in range(len(points)):
            xhat, yhat = points[i]
            if xhat == x or yhat == y:
                dis = abs(xhat - x) + abs(yhat - y)
                if dis < min_manhattan:
                    min_manhattan = dis
                    idx = i
        return idx