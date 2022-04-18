

import math
import os
import random
import re
import sys

#Insertion sort

def insertionSort1(n, arr):
    num = arr[n - 1]
    for j in range(n - 2, -1 , -1):
        if arr[j] > num:
            arr[j + 1] = arr[j]
        else:
            arr[j + 1] = num
        
        print(' '.join(map(str, arr)))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
