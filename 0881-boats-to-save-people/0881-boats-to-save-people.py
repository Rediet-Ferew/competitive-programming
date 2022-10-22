class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l = 0
        r = n - 1
        people_to_go = 0
        while l <= r:
            weight = people[r] + people[l]
            if weight <= limit:
                people_to_go += 1
                l += 1
                r -= 1
            else:
                people_to_go += 1
                r -= 1
        return people_to_go
            
                
            
            