tests = int(input())
def oddSwapSort():
    n = int(input())
    arr=list(map(int, input().split()))
    if n == 1:
        print('Yes')
        return
    odd = []
    even = []
    for i in range(n):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    if odd == sorted(odd) and even == sorted(even): 
        print("Yes")
    else: 
        print("No")
for _ in range(tests):
    oddSwapSort()
