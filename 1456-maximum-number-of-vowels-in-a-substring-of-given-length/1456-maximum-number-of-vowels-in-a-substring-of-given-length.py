class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        maxCount = 0
        for i, letter in enumerate(s):
            if letter in 'aeiou':
                count += 1
            if i >= k and s[i - k] in 'aeiou':
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount
        # for i in range(k):
        #     if s[i] in vowels:
        #         count += 1
        # for vowel in vowels:
        #     prefix_vowel[vowel] = 0
#         if k == 1:
#             for let in s:
#                 if let in vowels:
#                     return 1
        
#             temp = s[left:right + 1]
#             count = Counter(temp)
#             # print(count)
#             maximum = 0
#             for letter in count.keys():
#                 if letter in vowels:
#                     maximum += count[letter]
#                     result = max(maximum, result)
            
#         return result
        