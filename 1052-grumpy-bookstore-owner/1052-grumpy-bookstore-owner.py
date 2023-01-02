class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        pre_total = 0
        for i in range(n):
            if grumpy[i] == 0:
                pre_total += customers[i]
        
        left = 0
        right = 0
        max_customers = 0
        curr_sum = 0
        while right < minutes:
            if grumpy[right] == 1:
                curr_sum += customers[right]
            right += 1
        max_customers = max(curr_sum, max_customers)

        while right < n:
            if grumpy[right] == 1:
                curr_sum += customers[right]
            if grumpy[left] == 1:
                curr_sum -= customers[left]
            
            max_customers = max(max_customers, curr_sum)
            left += 1
            right += 1
        return max_customers + pre_total