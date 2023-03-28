

def mergeSort(left, right, arr, swaps):
    # nonlocal swaps
    mid = (left + right) // 2
    if left == right:
        return [arr[left]]
    else:
        left_list = mergeSort(left, mid, arr, swaps)
        right_list = mergeSort(mid + 1, right, arr, swaps)
    merged = []
    if right_list[-1] <= left_list[0]:
        merged.extend(right_list)
        merged.extend(left_list)
        swaps.append(1)
    else:
        merged.extend(left_list)
        merged.extend(right_list)
    # print(swaps)
    return merged

t = int(input())

for _ in range(t):
    n = int(input())
    swaps = []
    # temp = 0
    nums = list(map(int, input().split()))
    mrgd = mergeSort(0, n - 1, nums, swaps)
    # print(mrgd)
    # print(swaps)
    if mrgd == sorted(nums):
        print(sum(swaps))
    else:
        print(-1)



