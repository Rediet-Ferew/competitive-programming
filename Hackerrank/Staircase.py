#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    arr = [" "] * n  
    # Write your code here
    for i in range(n - 1, -1, -1):
        arr[i] = "#"
        print("".join(arr))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)