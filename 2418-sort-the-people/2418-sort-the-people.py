class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = []
        for n,h in zip(names,heights):
            pairs.append((h,n))
        pairs = sorted(pairs)[::-1]
        res = [val for key, val in pairs]
        return res