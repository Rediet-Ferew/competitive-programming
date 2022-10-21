class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Chars = {}
        for ch in strs:
            word = sorted(ch)
            word = "".join(word)
            if word not in Chars:
                Chars[word] = [ch]
            else:
                Chars[word].append(ch)
        result = []
        for key, val in Chars.items():
            result.append(val)
        return result
            
            