#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#
import math
def minTime(files, numCores, limit):
    # Write your code here
    print("files are",files,"core are ",numCores," limit is ",limit)
    sum1=0
    for i in files:
        if i >= numCores and limit>1:
            sum1 = sum1 + i/numCores
            limit=limit-1
            print("file is",i,"limit left",limit)

        else:
            sum1 = sum1 + i
        sum1 = int(math.ceil(sum1))

    return sum1

if __name__ == '__main__':
    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())
    print("sol")
    result = minTime(files, numCores, limit)
    print(result)

