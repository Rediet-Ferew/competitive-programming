class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_boxes = []
        answer = [0] * len(boxes)
        
        #store the index where the box is non empty
        for idx, num in enumerate(boxes):
            
            if num == '1':
                one_boxes.append(idx)
        
        #calculate the distance between each box and a box with one ball
        for i, n in enumerate(boxes):
            
            for idx in one_boxes:
                
                answer[i]  += abs(idx - i)
                
        return answer
                