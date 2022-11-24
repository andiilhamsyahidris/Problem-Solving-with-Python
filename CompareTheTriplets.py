import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    result = [];
    pointA = 0;
    pointB = 0;
    
    if a[0] > b[0]:
        pointA += 1        
    elif a[0] < b[0]:
        pointB += 1
    
    if a[1] > b[1]:
        pointA += 1
    elif a[1] < b[1]:
        pointB += 1
    
    if a[2] > b[2]:
        pointA += 1
    elif a[2] < b[2]:
        pointB += 1
    
    result.append(pointA)
    result.append(pointB)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()