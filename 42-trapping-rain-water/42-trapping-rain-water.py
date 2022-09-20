class Solution:
    def trap(self, height: List[int]) -> int:
        # setting boundaries and cheking the boundaries
        # it is to check the maxright and maxleft, taking the minimum of those and then 
        # substracting the ith height and that is the amount of water that can be trapped over that i
        n = len(height)
        left, right = 0, n - 1
        maxLeft = height[left]
        maxRight = height[right]
        
        count = 0
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                count += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                count += maxRight - height[right]
        return count