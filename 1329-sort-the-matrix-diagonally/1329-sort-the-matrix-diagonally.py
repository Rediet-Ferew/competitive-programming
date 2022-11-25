class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hashMap = {}
        rowLen, colLen = len(mat), len(mat[0])
        for r in range(rowLen):
            for c in range(colLen):
                diff = r - c
                if diff not in hashMap:
                    hashMap[diff] = [mat[r][c]]
                else:
                    hashMap[diff].append(mat[r][c])
        for key, val in hashMap.items():
            val.sort()
        for r in range(rowLen):
            for c in range(colLen):
                mat[r][c] = hashMap[r-c][0]
                hashMap[r-c] = hashMap[r-c][1:]
        return mat