class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        # print(prefix_xor)
        for j in range(len(queries)):
            left, right = queries[j]
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        return result