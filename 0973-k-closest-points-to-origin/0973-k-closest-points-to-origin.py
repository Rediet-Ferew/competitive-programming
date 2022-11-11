class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for point in points:
            distance = (point[0]**2) + (point[1]**2)
            dis.append((distance, point))
        
        dis = sorted(dis)
        res = []
        for i in range(k):
            res.append(dis[i][1])
        return res