class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [arr[0]]
        for i in range(1, len(arr)):
            val = xor[-1] ^ arr[i]
            xor.append(val)
        ans = [0] * len(queries)
        for j in range(len(queries)):
            l = queries[j][0]
            r = queries[j][1]
            if l == 0:
                ans[j] = xor[r]
            else:
                ans[j] = xor[l-1] ^ xor[r]
        return ans