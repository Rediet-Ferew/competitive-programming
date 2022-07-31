class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        from itertools import combinations
        result = []
        for person in combinations(people, 2):
            if person[0] + person[1] <= limit:
                result.append([person[0],person[1]])
                
        for i in range(len(result) - 1):
            for j in range(i + 1, len(result)):
                if sum(result[i]) == sum (result[j]):
                    result.remove(result[i])
        
        for k in range(len(result)):
            people.remove(result[k][0])
            people.remove(result[k][1])
       
        for per in people:
            if per <= limit:
                result.append([per])
        return len(result)
        