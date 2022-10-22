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
        # n = len(people)
        # people.sort()
        # max_people = []
        # left = 0
        # right = n - 1
        # while left <= right:
        #     weight = people[left] + people[right]
        #     if weight <= limit:
        #         max_people.append((people[left], people[right]))
        #         left += 1
        #         right -= 1
        #     else:
        #         max_people.append((people[right]))
        #         right -= 1
        # return len(max_people)
            
                
            
            