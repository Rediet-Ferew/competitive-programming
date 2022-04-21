class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= 1 and k < 10000:
            for i in range(0, len(points)):
                if (points[i][0] > -10000 and points[i][0] < 10000) and (points[i][1] > -10000 and points[i][1] < 10000):
                    minIndex = i
                    for j in range(i, len(points)):
                        dis1 = sqrt((points[j][0])**2 + (points[j][1])**2)
                        dis2 = sqrt((points[minIndex][0])**2 + (points[minIndex][1])**2)
                        if dis1 < dis2:
                            minIndex= j
                    points[i], points[minIndex] = points[minIndex], points[i]
            
        return points[:k]