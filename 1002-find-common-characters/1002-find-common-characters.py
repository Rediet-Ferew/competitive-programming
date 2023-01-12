class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        
        # for word in words[1:]:
        #     curr_count = Counter(word)
        #     for key, val in count.items():
        #         if key in curr_count:
        #             val = min(val, count[key])
        #         else:
        #             count.pop(key)
        
        for word in words[1:]:
            curr_count = {}

            for char in word:
                if char in count:
                    if char in curr_count:
                        curr_count[char] +=1
                    else:
                        curr_count[char] =1
                    if count[char]>1:
                        count[char] -=1
                    else:
                        count.pop(char)
            count = curr_count
        
        answer = []
        for key, val in count.items():
            for _ in range(val):
                answer.append(key)
        return answer
         