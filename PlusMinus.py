import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = []
    negative = []
    zero = []
    
    for i in range(0, len(arr)):
        if arr[i] > 0:
            positive.append(arr[i])
        elif arr[i] < 0:
            negative.append(arr[i])
        elif arr[i] == 0:
            zero.append(arr[i])
            
    
    print(len(positive)/len(arr))
    print(len(negative)/len(arr))
    print(len(zero)/len(arr))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)