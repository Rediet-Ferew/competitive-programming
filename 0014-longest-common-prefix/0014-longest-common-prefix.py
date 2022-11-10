class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = sorted(strs, key=len)
        ans = ""
        for i in range(len(shortest[0])):
            for word in strs:
                if word[i] != shortest[0][i]:
                    return ans
            ans += shortest[0][i]
        return ans