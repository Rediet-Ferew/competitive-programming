class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        [3, -2, 1, -5, 2, 4]
                   p
                n
        """
        pos = []
        neg = []
        final = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        for i in range(len(pos)):
            final.append(pos[i])
            final.append(neg[i])
        return final