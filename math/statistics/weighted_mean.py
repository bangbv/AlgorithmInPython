import math
import os
import random
import re
import sys


def weighted_mean(X, W):
    sum = 0
    sum_w = 0
    for i in range(len(X)):
        sum += X[i]*W[i]
        sum_w +=W[i]
    print(round(sum/sum_w, 1))
    # Write your code here


if __name__ == '__main__':
    # n = int(input().strip())
    #
    # vals = list(map(int, input().rstrip().split()))
    #
    # weights = list(map(int, input().rstrip().split()))
    vals = [1, 2, 3]
    weights = [5, 6, 7]

    weighted_mean(vals, weights)
