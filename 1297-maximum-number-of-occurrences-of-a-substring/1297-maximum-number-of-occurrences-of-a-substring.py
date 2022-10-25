class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        r = 0
        subs = []
        while r < len(s):
            for end in range(r + minSize - 1, min(len(s), r + maxSize)):
                if len(set(s[r:end+1])) <= maxLetters:
                    subs.append(s[r:end+1])
            r += 1
        if len(subs) == 0:
            return 0
        counter = Counter(subs)
        max_occ = max(counter.values())
        return max_occ