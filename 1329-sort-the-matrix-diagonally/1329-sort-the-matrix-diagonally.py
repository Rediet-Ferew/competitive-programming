class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hashMap = {}
        idx_set = {}
        rowLen, colLen = len(mat), len(mat[0])
        for r in range(rowLen):
            for c in range(colLen):
                diff = r - c
                if diff not in hashMap:
                    hashMap[diff] = [mat[r][c]]
                    idx_set[diff] = [(r,c)]
                else:
                    hashMap[diff].append(mat[r][c])
                    idx_set[diff].append((r,c))
        for key, val in hashMap.items():
            val.sort()
        for k, v in idx_set.items():
            for i in range(len(v)):
                r, c = v[i]
                mat[r][c] = hashMap[k][i]
        return mat