class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        l = 0
        while l < len(chars):
            r = l
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            chars[idx] = chars[l]
            idx += 1
            if r - l > 1:
                count = str(r - l)
                for c in count: 
                    chars[idx] = c
                    idx += 1
            l = r
        return idx