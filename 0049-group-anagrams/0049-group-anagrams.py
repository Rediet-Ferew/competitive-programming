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
            # if word in Chars:
            #     idx = Chars[word]
            #     temp = result[idx]
            #     print(temp)
            #     temp.append(s)
                
                
#         prefix = []
        
#         for i in range(len(strs)):
#             toAppend = sorted(strs[i])
#             prefix.append("".join(toAppend))
#         prefix = list(set(prefix))
#         prefixDict = {}
#         for word in prefix:
#             prefixDict[word] = []
#         for words in strs:
#             single = "".join(sorted(words))
#             if single in prefixDict.keys():
#                 prefixDict[single].append(words)
#         value = [val for val in prefixDict.values()]
#         return value
            