#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    checker = [0] * 4
    min_num = 0
    if n < 6:
        return (6 - n)
    else:
        for ch in password:
            if ch in numbers:
                checker[0] += 1
            elif ch in lower_case:
                checker[1] += 1
            elif ch in upper_case:
                checker[2] += 1
            elif ch in special_characters:
                checker[3] += 1
    for num in checker:
        if num == 0:
            min_num += 1
    return min_num
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
