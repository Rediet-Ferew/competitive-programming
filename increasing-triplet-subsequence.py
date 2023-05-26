class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        next_greater = ["-1"] * n
        prev_smaller = ["-1"] * n
        
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                
                v = stack.pop()
                next_greater[v] = nums[i]

            stack.append(i)
        
        st = []
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
               
                v = st.pop()
            if st:
                prev_smaller[i] = nums[st[-1]]
            st.append(i)
        
        for k in range(n):
            if prev_smaller[k] != "-1" and next_greater[k] != "-1":
                if prev_smaller[k] < nums[k] < next_greater[k]:
                    return True

        return False