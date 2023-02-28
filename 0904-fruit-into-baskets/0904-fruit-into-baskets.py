class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        count_map = {}
        left = 0
        max_fruits = 0
        
        for right in range(n):
            
            fruit = fruits[right]
            if fruit in count_map:
                count_map[fruit] += 1
            else:
                count_map[fruit] = 1
                
            cnt = len(count_map)
            while cnt > 2:
                fruit_left = fruits[left]
                
                if count_map[fruit_left] == 1:
                    count_map.pop(fruit_left)
                    cnt -= 1
                else:
                     count_map[fruit_left] -= 1
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits