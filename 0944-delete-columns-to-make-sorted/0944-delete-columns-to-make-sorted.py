class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        unsorted = 0
        n = len(strs[0])
        for i in range(n):
            # char = strs[0][i]
            ith_list = []
            for ch in strs:
                ith_list.append(ch[i])
            if sorted(ith_list) != ith_list:
                unsorted += 1
        return unsorted