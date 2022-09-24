

import math
import os
import random
import re
import sys

#Counting the number of occurences

def countingSort(arr):
    result = []
    for i in range(0, 100):
        counter = 0
        for j in range (0,  len(arr)):
            if i == arr[j]:
                counter += 1
        result.append(counter)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
