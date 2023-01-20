#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    num = arr[n - 1]
    idx = n - 2
    while idx >= 0:
        
        if arr[idx] > num:
            arr[idx + 1] = arr[idx]
            print(*arr)
            
        else:
            arr[idx + 1] = num
            break
        idx -= 1
    if idx == -1:
        arr[0] = num
    print(*arr)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
