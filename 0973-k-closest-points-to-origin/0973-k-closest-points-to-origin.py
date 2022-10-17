class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # minHeap = []
        # res = []
        # for point in points:
        #     dis = (point[0] ** 2) + (point[1] ** 2)
        #     minHeap.append([dis, point[0], point[1]])
        # heapq.heapify(minHeap)
        # while k > 0:
        #     dis, x, y = heapq.heappop(minHeap)
        #     res.append([x,y])
        #     k -= 1
        # return res
        distances = []
        for point in points:
            dis = (point[0] ** 2) + (point[1] ** 2)
            distances.append((dis, point))
        
        sortDistance = sorted(distances, key = lambda x : x[0],reverse=False)
        # print(hello)
        # print(distances[hello[0]])
        res = [p[1] for p in sortDistance[: k]]
        # i = 0
        # while k > 0 and i < len(sortDistance):
        #     idx = sortDistance[i][1]
        #     res.append(points[idx])
        #     i += 1
        #     k -= 1
        return res
            
        