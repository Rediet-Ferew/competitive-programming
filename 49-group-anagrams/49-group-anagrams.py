class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        prefix = []
        
        for i in range(len(strs)):
            toAppend = sorted(strs[i])
            prefix.append("".join(toAppend))
        prefix = list(set(prefix))
        prefixDict = {}
        for word in prefix:
            prefixDict[word] = []
        for words in strs:
            single = "".join(sorted(words))
            if single in prefixDict.keys():
                prefixDict[single].append(words)
        value = [val for val in prefixDict.values()]
        return value
            