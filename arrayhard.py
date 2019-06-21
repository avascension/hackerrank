#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

        arr = sorted(queries,key=lambda x: x[0])

            curr_index = 0
                bound_index = 0
                    bound_right = arr[0][1]
                        runningtotal = 0
                            maxsofar = 0

                                for entry in arr:
                                            if entry[0] <= bound_right:
                                                            runningtotal = runningtotal + entry[2]
                                                                        maxsofar = max(maxsofar, runningtotal)
                                                                                else:
                                                                                                while bound_index < curr_index and arr[bound_index][1] < entry[0]:
                                                                                                                    runningtotal = runningtotal - arr[bound_index][2]
                                                                                                                                    bound_index = bound_index + 1
                                                                                                                                                bound_right = arr[bound_index][1]
                                                                                                                                                            runningtotal = runningtotal + entry[2]
                                                                                                                                                                        maxsofar = max(maxsofar, runningtotal)
                                                                                                                                                                                curr_index = curr_index + 1
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

