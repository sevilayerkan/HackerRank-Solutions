#!/bin/python3

import math
import os
import random
import re
import sys


def bubbleSort(li):
    numSwaps = 0
    l = len(li)
    for i in range(0, l):
        for j in range(0, l-1):
            if (li[j] > li[j+1]):
                swap = li[j]
                li[j] = li[j+1]
                li[j+1] = swap
                numSwaps = numSwaps + 1

        if (numSwaps == 0):
            break

    print("Array is sorted in " + str(numSwaps) + " swaps.")
    print("First Element: " + str(li[0]))
    print("Last Element: " + str(li[-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    bubbleSort(a)
