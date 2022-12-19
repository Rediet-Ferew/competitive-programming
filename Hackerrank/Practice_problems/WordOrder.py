# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
count = {}
for i in range(n):
    word = input()
    count[word] = 1 + count.get(word, 0) 
print(len(count))
for k, v in count.items():
    print(v, end=' ')
