class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        max_people = []
        left = 0
        right = n - 1
        while left <= right:
            weight = people[left] + people[right]
            if weight <= limit:
                max_people.append((people[left], people[right]))
                left += 1
                right -= 1
            else:
                max_people.append((people[right]))
                right -= 1
        return len(max_people)
            
                
            
            