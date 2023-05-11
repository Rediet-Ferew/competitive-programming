class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incomings = [0] * numCourses
        adj_list = collections.defaultdict(list)
        ans = []
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            incomings[course] += 1
        
        q = collections.deque()
        
        for i in range(len(incomings)):
            if incomings[i] == 0:
                q.append(i)
                ans.append(i)
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                val = q.popleft()
                for crs in adj_list[val]:
                    incomings[crs] -= 1
                    if incomings[crs] == 0:
                        ans.append(crs)
                        q.append(crs)
        if len(ans) != numCourses:
            return False
        return True