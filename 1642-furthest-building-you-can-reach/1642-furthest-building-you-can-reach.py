class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        counter = 0
        furthest = []
        heapq.heapify(furthest)
        if len(heights) == 1:
            return 0
        for i in range(len(heights) - 1):
            if heights[i] >= heights[i + 1]:
                continue
            else:
                diff = heights[i + 1] - heights[i]
                heapq.heappush(furthest, diff)
            if len(furthest) > ladders:
                min_height = heapq.heappop(furthest)
                bricks -= min_height
            if bricks < 0:
                return i
        
        return len(heights) - 1
       
#         newList.sort()
#         print(newList)
#         while ladders > 0  and newList:
#             newList.pop()
#             ladders -= 1
#             counter += 1
#         print(counter)
#         print(newList)
#         j = 0
#         while j < len(newList):
#             if bricks >= newList[j]:
#                 bricks -= newList[j]
#                 counter += 1
#             j += 1
        
            
    