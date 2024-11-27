#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_s = scores[0] 
    max_s = scores[0]
    cmax = 0
    cmin = 0
  
    for score in scores:
        if score < min_s:
            min_s = min(score,min_s)
            cmin +=1
        elif  score > max_s:
            max_s = max(score,max_s)
            cmax +=1
    return ( cmax, cmin)
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
