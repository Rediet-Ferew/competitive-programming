# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input())
English = set(input().split(" "))
n2 = int(input())
French = set(input().split(" "))

Union = English.union(French)
print(len(Union))
