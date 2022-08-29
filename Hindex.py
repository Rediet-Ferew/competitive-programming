class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations = sorted(citations)
        for paper, cite in enumerate(citations):
            if n - paper <= cite:
                return n - paper
        return 0
        