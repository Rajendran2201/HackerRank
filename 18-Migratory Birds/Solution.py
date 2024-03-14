#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    set1 = set(arr)
    count = 0 
    counts = []
    for i in set1 :
        if i in arr:
            count = arr.count(i)
            counts.append(count)
    my_dict = dict(zip(set1, counts))
    all_values = my_dict.values()
    max_value = max(all_values)
    for key, values in my_dict.items():
        if values == max_value:
            return key
        
         
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
