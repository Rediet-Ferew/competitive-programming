class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            word_sort = sorted(word)
            curr_word = "".join(word_sort)
            if curr_word not in anagrams:
                anagrams[curr_word] = [word]
            else:
                anagrams[curr_word].append(word)
        res = []
        res = [val for key, val in anagrams.items()]
        return res