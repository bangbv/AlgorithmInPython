#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/s10-quartiles/problem
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    sa = sorted(arr)
    print(sa)
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # data = list(map(int, input().rstrip().split()))
    data = [9, 5, 7, 1, 3]

    quartiles(data)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
