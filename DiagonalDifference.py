import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    resultA = 0
    resultB = 0
    
    for i in range(0, len(arr)):
        resultA += arr[i][i]
    for j in range(0, len(arr)):
        resultB += arr[j][len(arr) - 1 - j]
    
    return abs(resultA - resultB)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()