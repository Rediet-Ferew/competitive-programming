class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        top, left = 0, 0
        bottom, right = rowLen, colLen
        ans = []
        
        while (top < bottom) and (left < right):
            for idx in range(left, right):
                ans.append(matrix[top][idx])
                
            top += 1
            
            for i in range(top, bottom):
                # print()
                ans.append(matrix[i][right - 1])
            
            right -= 1
            
            for j in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][j])
            
            bottom -= 1
            
            for k in range(bottom - 1, top - 1, -1):
                ans.append(matrix[k][left])
                
            left += 1
            
            if top == bottom and left == right:
                break
                
        indx =  rowLen * colLen     
        return (ans[:indx])