class Solution:
    def trap(self, height: List[int]) -> int:
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
        # for i in range(1, n):
        #     maxLeft.append(max(height[: i]))
        # for i in range(0, n - 1):
        #     maxRight.append(max(height[i + 1: ]))
        # maxRight.append(0)
        # for k in range(len(maxLeft)):
        #     minimum.append(min(maxLeft[k], maxRight[k]))
        # for k in range(n):
        #     diffMin = (min(maxLeft[k], maxRight[k])) - height[k] 
        #     if diffMin > 0:
        #         count += diffMin
        # return count
        # for l in range(n):
        #     diff = minimum[l] - height[l]
        #     if  diff > 0:
        #         count += diff
        return count