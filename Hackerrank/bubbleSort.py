

import math
import os
import random
import re
import sys

#Counts number of swaps

def countSwaps(a):
    next = 0
    for i in range(0, len(a) - 1):
        for j in range (0, len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] =  a[j+1], a[j]
                next+=1

    print("Array is sorted in", next, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
