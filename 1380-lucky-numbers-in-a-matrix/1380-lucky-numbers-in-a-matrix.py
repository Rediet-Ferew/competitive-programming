class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        min_list = []
        max_list = []
        lucky = []
        for r in matrix:
            min_list.append(min(r))
        for c in range(col):
            curr_max = float('-inf')
            for r in range(row):
                curr_max = max(curr_max, matrix[r][c])
            max_list.append(curr_max)
        # print(min_list) #see row index in min_list
        # print(max_list) #see col index in max_list
        for i in range(row):
            for j in range(col):
                if min_list[i] == max_list[j] == matrix[i][j]:
                    lucky.append(matrix[i][j])
        return lucky