#!/bin/python3

import math
import os
import random
import re
import sys

# Creation of hourglass-shaped sums
def get_sum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum
    
# Complete the hourglassSum function below.
def hourglassSum(arr):
    current_max_sum = -100
    for i in range(1,5):
        for j in range(1,5):
            sum = get_sum(arr, i, j)
            if sum > current_max_sum:
                current_max_sum = sum
    return current_max_sum
            
            

            
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
