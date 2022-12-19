# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
nums = input().split(" ")
count = {}
for num in nums:
    num = int(num)
    count[num] = 1 + count.get(num, 0)
for k, v in count.items():
    if v == 1:
        print(k)
        break
