#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # so smart, could sort the list first by ascending order therefore can check overlap
    arr = sorted(queries,key=lambda x: x[0])
    maxsofar = 0
    runningtotal = 0
    currentpost = arr[0][2]
    rangeright = arr[0][1]

    for entry in arr:
        if entry[0] <= rangeright:
            runningtotal = runningtotal + entry[2]
            maxsofar = max(maxsofar,runningtotal)
        else:
            rangeright = entry[1]
            runningtotal = runningtotal + entry[2] - currentpost
            currentpost = entry[2]
            maxsofar = max(maxsofar,runningtotal)
    print(maxsofar)
    return maxsofar
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

