#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maximum = max(arr)
    minimum = min(arr)
    total_sum = sum(arr)
    max_sum = total_sum - minimum
    min_sum = total_sum - maximum
    print(min_sum, max_sum)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
