test_cases = int(input())

for _ in range(test_cases):
    
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    #The problem is all about finding the longest strictly increasing subarray with size k
    #the thing is the front element is always multiplied by two
    #the division of a[i + 1]/a[i] is always 2
    #then a[i + 1] * 2 should be greater than a[i] for this case
    
    longest_in = [1] * n
    idx = 0
    
    while idx < n - 1:
        #count the longest strictly increasing subarray
        #and increment the value at the started index until the increasing pattern is invalid
        curr = idx
        while (idx < len(nums) - 1) and ((2 * nums[idx + 1]) > nums[idx]):
            longest_in[curr] += 1
            idx += 1
        idx += 1
    
    
    answer = 0
    
    for counter in longest_in:
        
        if counter >= k + 1:
            answer += counter - k 
    # print(longest_in)
    print(answer)
