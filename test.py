#!/bin/python3

import math
import os
import random
import re
import sys

arr=[]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = -63
    for i in range(4):
        for j in range(4):

            # sum of top 3 elements
            top = sum(arr[i][j:j + 3])

            # sum of the mid element
            mid = arr[i + 1][j + 1]

            # sum of bottom 3 elements
            bottom = sum(arr[i + 2][j:j + 3])

            hourglass = top + mid + bottom

            if hourglass > maxSum:
                maxSum = hourglass

    return maxSum

with open("array.txt",) as f:
    Myarray = f.read().rstrip().splitlines()

for x in Myarray:
    x = list(map(int,x.split()))
    arr.append(x)

print(arr)

result = hourglassSum(arr)

print(result)




