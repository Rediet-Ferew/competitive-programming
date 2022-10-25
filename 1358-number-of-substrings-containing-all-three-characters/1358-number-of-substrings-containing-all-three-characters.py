class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = {}
        l = 0
        r = 0
        output = 0
        while r < n:
            count[s[r]] = 1 + count.get(s[r], 0)
            while len(count) == 3:
                output += (n - r)
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
            r += 1
        return output
        
            