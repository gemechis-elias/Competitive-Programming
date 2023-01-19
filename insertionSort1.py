#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    pos=n-1
    current_value=arr[pos]
    while current_value<arr[pos-1] and pos>0:
        arr[pos]=arr[pos-1]
        pos-=1
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
    arr[pos]=current_value
    for i in range(len(arr)):
            print(arr[i],end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
