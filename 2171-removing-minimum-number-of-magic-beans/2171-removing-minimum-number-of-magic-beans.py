class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        if len(set(beans)) == 1:
            return 0
        suffix = sum(beans)
        prefix = 0
        removal = float("inf")
        for i in range(n):
            suffix -= beans[i]
            curr_rem = prefix + suffix - ((n-i-1)*beans[i])
            removal = min(removal, curr_rem)
            prefix += beans[i]
        return removal
        
        