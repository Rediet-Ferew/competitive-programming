#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def digitSum(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return total
def SuperDigit(sum_):
    if len(str(sum_)) == 1:
        return sum_
    else:
        return SuperDigit(digitSum(str(sum_)))
def superDigit(n, k):
    
    sum_ = digitSum(n)
    sum_super = SuperDigit(sum_)
    sum_super *= k
    
    if len(str(sum_super)) > 1:
        return SuperDigit(sum_super)
    
    else:
        return sum_super
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
